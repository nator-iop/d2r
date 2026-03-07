# D2R Loot Filters

Loot filters for Diablo 2 Resurrected, targeting three builds: **Warlock** (Echoing Strike), **Hammerdin** (Blessed Hammer), and **Javazon** (Lightning Fury).

## Filters

### nator-bis
The strict endgame filter. Shows only:
- Best-in-slot unique and set items for the three builds
- Valuable/grail unique and set items you never want to miss (Tyrael's Might, Death's Fathom, Griffon's Eye, etc.)
- Merc gear (Andariel's Visage, Reaper's Toll, Guillaume's Face, etc.)
- Elite runeword bases (Monarch, Archon Plate, Thresher, Thunder Maul, etc.)
- Rare+ rings, amulets, and jewels
- Magic charms

Everything else is hidden.

### nator-combined
Same as the BiS filter, plus toggleable rules you can turn on/off in-game:

| Rule | Default | What it shows |
|------|---------|---------------|
| Pre-BiS Unique Normal | off | Budget uniques: Bloodfist, Goblin Toe, Gull, Tarnhelm, Nightsmoke, Spectral Shard |
| Pre-BiS Unique Except | off | Budget exceptionals: Rockstopper, Peasant Crown, Moser's, Duriel's Shell, Blade of Ali Baba, Suicide Branch |
| Pre-BiS Bases Except | off | Socketed exceptional bases for merc/mid-game runewords: Death Mask, Grim Helm, Serpentskin, Cuirass, Mage Plate |
| Lvl Bases Normal | off | Early runeword bases: Crystal Sword, Broad Sword, shields, polearms (Spirit, Insight, Ancients' Pledge) |
| Lvl Bases Exceptional | off | Better polearm bases for Insight: Bill, Battle Scythe, Partizan, Bec-de-Corbin, Grim Scythe |

Turn these on at the start of a new season, then toggle them off as you gear up.

### nator-farm
A broader farming filter that shows more items. Less strict than the BiS filter.

## How to import

1. Open the filter file on GitHub and click the "Raw" button
2. Select all and copy to clipboard
3. In D2R, go to Options > Loot Filter > Import from Clipboard

## Rule naming convention

Rules are prefixed by category:
- **BiS** — endgame best-in-slot gear (always on)
- **Pre-BiS** — budget/mid-game gear (toggle on when needed)
- **Lvl** — leveling bases (toggle on for new season)
- No prefix — general rules (Accessories, Charms, Hide All)

## Filter name character limit

D2R has a ~15 character limit on the filter name field. Keep it short.
