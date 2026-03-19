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
- Build: `python3 lootfilter/build.py` (resolves names → codes, generates JSON, auto-bumps version)
- Targets builds: Warlock, Sorc, Hammerdin, Javazon, Frenzy (plus merc gear and ultra-rare drops)
- YAML organizes items per-build; build script merges into 3 rules: Unique, Set, Bases
- Warlock items use `equipmentCategory: ["warlo"]` (category-based, not item codes)
- Rule order: Unicorn Drops → Unique/Set/Bases → Merc → Warlock → Accessories → Set Amulets → Rare Diadems → disabled rules → Hide All
- Toggleable disabled rules for farming, pre-BiS gear, and leveling bases
- Data files (Armor.txt, Weapons.txt, UniqueItems.txt, SetItems.txt) are local for code lookups
- Overrides in YAML handle D2R items and 1.13 data file typos/old names
- **Hard limit: 32 rules max** — game silently truncates beyond this (Hide All must be last)

## Reviewed and kept (not BiS but intentionally included)

- Nosferatu's Coil — good melee belt, kept by choice
- The Grandfather — iconic drop, in Unicorn Drops
- Mang Song's Lesson — rare caster staff, in Unicorn Drops
- Wraithstep — D2R-added unique, kept
