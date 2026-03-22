#!/usr/bin/env python3
"""Build nator.filter.json from nator.source.yaml

Usage: python3 build/build.py
"""

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).parent.parent
BUILD_DIR = ROOT / "build"
DATA_DIR = ROOT / "data"
OUT_DIR = ROOT / "lootfilter"


def normalize(s):
    """Normalize name for fuzzy matching: lowercase, strip spaces/punctuation."""
    return s.lower().replace(" ", "").replace("'", "").replace("-", "")


def load_tsv(filename, key_col, val_col):
    """Load a TSV data file as {col[key]: col[val]}."""
    result = {}
    with open(DATA_DIR / filename, encoding="latin-1") as f:
        header = f.readline().strip().split("\t")
        ki = header.index(key_col)
        vi = header.index(val_col)
        for line in f:
            cols = line.split("\t")
            if len(cols) > max(ki, vi):
                k, v = cols[ki].strip(), cols[vi].strip()
                if k and v:
                    result[k] = v
    return result


class Resolver:
    def __init__(self, overrides):
        self.overrides = overrides or {}
        self.bases = {
            **load_tsv("Armor.txt", "name", "code"),
            **load_tsv("Weapons.txt", "name", "code"),
        }
        self.uniques = load_tsv("UniqueItems.txt", "index", "code")
        self.sets = load_tsv("SetItems.txt", "index", "item")
        self.errors = []

    def resolve(self, name, context=""):
        """Resolve item name to 3-letter code."""
        # Overrides first (handles D2R items, typos, renamed items)
        if name in self.overrides:
            return self.overrides[name]

        norm = normalize(name)
        for table in [self.uniques, self.sets, self.bases]:
            # Exact match
            if name in table:
                return table[name]
            # Normalized match (handles spacing/case differences)
            for key, code in table.items():
                if normalize(key) == norm:
                    return code

        self.errors.append(f"  '{name}' ({context})")
        return None

    def resolve_list(self, names, context=""):
        """Resolve list of names to deduped codes, preserving order."""
        codes = []
        seen = set()
        for name in names or []:
            code = self.resolve(name, context)
            if code and code not in seen:
                codes.append(code)
                seen.add(code)
        return codes


def make_rule(name, codes, *, enabled=True, rarity=None, eth=False,
              quality=None, categories=None):
    """Create a show rule."""
    rule = {
        "name": name,
        "enabled": enabled,
        "ruleType": "show",
        "filterEtherealSocketed": eth,
    }
    if rarity:
        rule["equipmentRarity"] = rarity
    if quality:
        rule["equipmentQuality"] = quality
    if categories:
        rule["equipmentCategory"] = categories
    if codes:
        rule["equipmentItemCode"] = codes
    return rule


def build(source):
    r = Resolver(source.get("overrides"))
    rules = []

    # White bases (to Larzuk — non-eth, non-socketed)
    if items := source.get("whites"):
        codes = r.resolve_list(items, "whites")
        rules.append(make_rule("Whites", codes,
                               rarity=["normal", "hiQuality"]))

    # Unicorn drops
    if u := source.get("unicorn", {}):
        if items := u.get("unique"):
            codes = r.resolve_list(items, "unicorn")
            rules.append(make_rule("Unicorn Drops", codes, rarity=["unique"]))

    # Merge common + all builds into 3 rules (YAML keeps per-build for readability)
    all_unique = list(source.get("common", {}).get("unique", []))
    all_set = list(source.get("common", {}).get("set", []))
    all_bases = list(source.get("common", {}).get("bases", []))

    for bname in source.get("build_order", []):
        build_cfg = source.get("builds", {}).get(bname, {})
        all_unique.extend(build_cfg.get("unique", []))
        all_set.extend(build_cfg.get("set", []))
        all_bases.extend(build_cfg.get("bases", []))

    if all_unique:
        codes = r.resolve_list(all_unique, "unique")
        rules.append(make_rule("Unique", codes, rarity=["unique"]))
    if all_set:
        codes = r.resolve_list(all_set, "set")
        rules.append(make_rule("Set", codes, rarity=["set"]))
    if all_bases:
        codes = r.resolve_list(all_bases, "bases")
        rules.append(make_rule("Bases", codes, eth=True))

    # Merc (eth uniques)
    if m := source.get("merc", {}):
        if items := m.get("unique"):
            codes = r.resolve_list(items, "merc.unique")
            rules.append(make_rule("Merc Eth Unique", codes,
                                   rarity=["unique"], eth=True,
                                   quality=["elite", "exceptional"]))

    # Rule count check
    n_other = len(source.get("other_rules", []))
    n_total = len(rules) + n_other
    if n_total > 32:
        print(f"WARNING: {n_total} rules exceeds 32-rule game limit!")

    # Other rules (passthrough, with optional name resolution)
    for rule in source.get("other_rules", []):
        rule = dict(rule)
        if "items" in rule:
            names = rule.pop("items")
            codes = r.resolve_list(names, rule.get("name", "other"))
            rule["equipmentItemCode"] = codes
        rules.append(rule)

    if r.errors:
        print("Failed to resolve:")
        for e in r.errors:
            print(e)
        sys.exit(1)

    return {"name": source["name"], "rules": rules}


def bump_version(source, src_path):
    """Auto-increment version number in source YAML."""
    name = source["name"]
    m = re.search(r"(v)(\d+)", name)
    if not m:
        return
    old_ver = int(m.group(2))
    new_ver = old_ver + 1
    new_name = name[:m.start(2)] + str(new_ver) + name[m.end(2):]
    source["name"] = new_name

    # Update YAML file in place
    text = src_path.read_text()
    text = text.replace(f"name: {name}", f"name: {new_name}", 1)
    src_path.write_text(text)
    print(f"Version: {name} -> {new_name}")


def build_filter(src_path):
    """Build a single filter from a source YAML file."""
    with open(src_path) as f:
        source = yaml.safe_load(f)

    result = build(source)

    stem = src_path.stem.replace(".source", "")
    out = OUT_DIR / f"{stem}.filter.json"

    # Only bump version if output changed
    old_json = ""
    if out.exists():
        old_json = out.read_text()

    new_json = json.dumps(result, indent=4) + "\n"

    # Compare without version in name to detect real changes
    old_comparable = re.sub(r'"name": ".*?"', '"name": ""', old_json)
    new_comparable = re.sub(r'"name": ".*?"', '"name": ""', new_json)

    if old_comparable != new_comparable:
        bump_version(source, src_path)
        result["name"] = source["name"]
        new_json = json.dumps(result, indent=4) + "\n"
        out.write_text(new_json)
        n_rules = len(result["rules"])
        n_codes = sum(len(r.get("equipmentItemCode", [])) for r in result["rules"])
        print(f"Generated {out.name}: {n_rules} rules, {n_codes} item codes")
    else:
        print(f"No changes: {out.name}")


def main():
    sources = sorted(BUILD_DIR.glob("*.source.yaml"))
    if not sources:
        print("No .source.yaml files found in build/")
        sys.exit(1)
    for src in sources:
        build_filter(src)


if __name__ == "__main__":
    main()
