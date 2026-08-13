# Spirit Card Builder (local)

Local-only UI for scaffolding Spirit PTCGO Python card scripts using existing factories and similar card scripts from the codebase.

## Run

```bash
cd tools/card-builder
npm install
npm run sync-data              # once (or when you want catalog updates)
npm run generate:implemented-ids
npm run dev
```

Opens at [http://localhost:5174](http://localhost:5174).

## Browse cards (no live API)

Catalog data comes from a local clone of [PokemonTCG/pokemon-tcg-data](https://github.com/PokemonTCG/pokemon-tcg-data):

1. `npm run sync-data` shallow-clones/updates into `data/pokemon-tcg-data`
2. Vite serves that folder at `/tcg-data/*`
3. Browse series → set → card (or search by name) to pre-fill the generator

Reference art uses the `images.pokemontcg.io` URLs already in that JSON. On **Save**, the large image is downloaded to `spirit/assets/cards/<SET>/<Stem>_<number>.png`.

Implemented cards (from `implementedCardIds.json`) are greyed out in the card grid. Regenerate after adding scripts:

```bash
npm run generate:implemented-ids
```

## Generation rules

- Attack, Ability, and Trainer effect text uses a matching Spirit factory prefab when available (`draw_attack`, `condition_attack`, `flip_damage`, `snipe_attack`, `heal_item`, `search_to_hand`, …).
- If no prefab matches, the builder searches existing scripts under `spirit/game/scripts/cards/**` for a strong same-kind `game_text` match and reuses that `effect=` expression (plus helpers/imports when possible).
- If neither a prefab nor a sufficiently similar script is found, text is preserved with `effect=unimplemented`.
- Empty attack text (damage-only) emits no `effect`.
- Output is a Python `*CardDef` script aligned with `spirit/tools/import_set.py` conventions (GUID via `uuid5(DNS, "spirit.ptcgo." + catalogId)`).

## Prefab UI

For each attack, ability, or Trainer effect:

1. Enter effect text and click **Match from text**, or
2. Manually **Add** a prefab from the dropdown and edit parameters.

Then click **Generate card** and copy the Python output.

Click **Save to spirit scripts** to write the `.py` file under `spirit/game/scripts/cards/<SET>/` and download art. Existing files require confirmation before overwrite. If the Spirit set is missing from `sets.json`, the UI warns (formats are not auto-edited).

## Reprints

When another printing of the same card name already exists in the target set folder, enable **Save as a Spirit reprint() stub** to emit:

```python
from spirit.game.data_utils import reprint, sibling_card
card = reprint(sibling_card(__file__, "OtherCard_12.py"), collector_number=..., rarity=...)
```
