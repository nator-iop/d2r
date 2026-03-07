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

## Questionable items in BiS filter (to review later)

Unique rules contain some codes that may not belong:
- `xsh` (Lidless Wall), `xsk` (Blackhorn's Face), `9cr` (Ginther's Rift) — not BiS for any build, not on maxroll valuable list
- `ulg` (Bramble Mitts), `uth` (Lacquered Plate), `xmg` (Heavy Bracers) in Unique rules — no notable unique on these bases; they only matter in the Set rules (Laying of Hands, Tal Rasha's Guardianship, Trang-Oul's Claws)
- `uvc` (Nosferatu's Coil), `xtp` (Que-Hegan's Wisdom) — not top BiS, not on valuable list
- `7gd` (The Grandfather), `7gm` (Earthshifter/Cranium Basher), `7wh` (Stone Crusher/Schaefer's), `6ws` (Mang Song's Lesson) — not BiS, not on valuable list but notable drops
- `utb`, `utc` in Unique Elite — can't identify a unique on these bases (utc is Trang-Oul's Girth which is a set item, now correctly added to Set Elite)
