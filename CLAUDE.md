# D2R Loot Filters

## References

- Item codes (Armor.txt): lootfilter/Armor.txt (from github.com/fabd/diablo2)
- Item codes (Weapons.txt): lootfilter/Weapons.txt
- Unique items: lootfilter/UniqueItems.txt
- Set items: lootfilter/SetItems.txt
- Endgame loot filter reference: https://github.com/Roguecor/d2r-endgame-loot-filter
- Warlock build (Echoing Strike): https://maxroll.gg/d2/guides/echoing-strike-warlock-guide
- Hammerdin build: https://maxroll.gg/d2/guides/blessed-hammer-paladin
- Javazon build: https://maxroll.gg/d2/guides/lightning-fury-amazon-guide
- Frenzy Barb build: https://maxroll.gg/d2/guides/frenzy-barbarian
- Valuable unique/set items: https://maxroll.gg/d2/items/valuable-unique-set-items
- Item codes (all types): lootfilter/Diablo 2 Items Codes.html
- Item base lookup: https://diablo.fandom.com/wiki/ (append item name, e.g. Bramble_Mitts)

## Filter conventions

- All items are shown by default. Show rules trump hide rules. Rule order does not matter
- `filterEtherealSocketed: true` means the rule applies to ethereal/socketed items
- `equipmentItemCode` uses 3-letter codes from the game data files (Armor.txt, Weapons.txt)
- Quality tiers: normal, exceptional, elite
- Item code prefixes: normal = no prefix, exceptional = x/z/8/9 prefix, elite = u/7/6 prefix (varies by item type)

## Nator filter

- Source of truth: `lootfilter/nator.source.yaml` (human-readable item names)
- Generated output: `lootfilter/nator.filter.json` (do not edit directly)
- Build: `python3 lootfilter/build.py` (resolves names → codes, generates JSON)
- Bump version in `nator.source.yaml` `name` field on each commit
- Targets builds: Warlock, Sorc, Hammerdin, Javazon, Frenzy (plus merc gear and ultra-rare drops)
- Rule structure: Unicorn Drops → Common (Unique/Set/Bases) → Per-build (Unique/Set/Bases) → Merc → Other
- Warlock items use `equipmentCategory: ["warlo"]` (category-based, not item codes)
- Toggleable disabled rules for farming, pre-BiS gear, and leveling bases
- Data files (Armor.txt, Weapons.txt, UniqueItems.txt, SetItems.txt) are local for code lookups
- Overrides in YAML handle D2R items and 1.13 data file typos/old names
- **Hard limit: 32 rules max** — game silently truncates beyond this (Hide All must be last)

## Reviewed and kept (not BiS but intentionally included)

- `uvc` (Nosferatu's Coil) — good melee belt, kept by choice
- `7gd` (The Grandfather) — iconic drop, kept by choice
- `6ws` (Mang Song's Lesson) — rare caster staff, kept by choice
- `utb` (Mirrored Boots / Wraithstep) — D2R-added unique, kept
