# D2R Loot Filters

## References

- Item codes (Armor.txt): https://github.com/fabd/diablo2/blob/master/code/d2_113_data/Armor.txt
- Item codes (Weapons.txt): https://github.com/fabd/diablo2/blob/master/code/d2_113_data/Weapons.txt
- Endgame loot filter reference: https://github.com/Roguecor/d2r-endgame-loot-filter
- Warlock build (Echoing Strike): https://maxroll.gg/d2/guides/echoing-strike-warlock-guide
- Hammerdin build: https://maxroll.gg/d2/guides/blessed-hammer-paladin
- Javazon build: https://maxroll.gg/d2/guides/lightning-fury-amazon-guide
- Valuable unique/set items: https://maxroll.gg/d2/items/valuable-unique-set-items

## Filter conventions

- Bump the version number in the filter `name` field on each commit (e.g. "Nator BiS v1" -> "Nator BiS v2")
- All items are shown by default. Show rules trump hide rules. Rule order does not matter
- `filterEtherealSocketed: true` means the rule applies to ethereal/socketed items
- `equipmentItemCode` uses 3-letter codes from the game data files (Armor.txt, Weapons.txt)
- Quality tiers: normal, exceptional, elite
- Item code prefixes: normal = no prefix, exceptional = x/z/8/9 prefix, elite = u/7/6 prefix (varies by item type)

## Nator BiS filter

- Targets three builds: Warlock, Hammerdin, Javazon (plus merc gear and ultra-rare drops)
- Unique and set items are in separate rules to avoid showing non-BiS items that share a base type
- Runeword bases are limited to specific desirable bases, not all elite socketed items
