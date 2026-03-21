# D2R Loot Filters

Loot filter for Diablo 2 Resurrected, targeting five builds: **Warlock** (Echoing Strike), **Sorc**, **Hammerdin** (Blessed Hammer), **Javazon** (Lightning Fury), and **Frenzy Barb**.

## How it works

The filter is maintained as a human-readable YAML file (`build/nator.source.yaml`) with item names organized by build. A build script resolves names to game codes and generates the filter JSON.

```
Edit build/nator.source.yaml → Run python3 build/build.py → Import lootfilter/nator.filter.json
```

The build script auto-increments the version number on each run.

## What's always on

| Rule | What it shows |
|------|---------------|
| Unicorn Drops | Ultra-rare uniques you never want to miss (Tyrael's Might, Griffon's Eye, Windforce, etc.) |
| Unique | Valuable/build uniques across all five builds |
| Set | Valuable/build set items (Tal Rasha, Guillaume's, IK, Griswold's, etc.) |
| Bases | Elite runeword bases (Monarch, Archon Plate, Phase Blade, Thresher, etc.) |
| Merc Eth Unique | Ethereal merc weapons/armor (Reaper's Toll, Shaftstop, etc.) |
| Warlock Class Items | All rare/set/unique Warlock class items |
| Accessories | Rare/unique rings, amulets, and jewels |
| Set Amulets | Set amulets |
| Rare Diadems | Rare diadems (for GG affixes) |

Everything else is hidden.

## Toggleable rules (disabled by default)

| Rule | What it shows |
|------|---------------|
| Farm Uni/Set Elite | ALL elite unique/set items (for trading/identifying) |
| Farm Bases Elite | ALL elite socketed items (broad runeword base search) |
| Farm Magic Jewels | Magic jewels (for facets) |
| Farm Magic Rings | Magic rings |
| Farm Potions | All potions except minor |
| Pre-BiS Unique Normal | Budget normal uniques |
| Pre-BiS Unique Except | Budget exceptional uniques |
| Pre-BiS Bases Normal | Normal runeword bases (Flail for HotO) |
| Pre-BiS Bases Except | Exceptional runeword bases |
| Lvl Bases Normal | Early bases (Crystal Sword, shields, polearms) |
| Lvl Bases Exceptional | Better polearm bases for Insight |

## How to import

1. Open `lootfilter/nator.filter.json` on GitHub and click "Raw"
2. Select all and copy to clipboard
3. In D2R, go to Options > Loot Filter > Import from Clipboard

## Limits

- **32 rules max** — game silently truncates beyond this
- **~15 char filter name** — keep the name field short
