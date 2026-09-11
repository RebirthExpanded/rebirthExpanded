"""Aqua Patch (SM - Guardians Rising 119/145 -- JP SM2L 048/050).

Item.

  "Attach a Water Energy card from your discard pile to 1 of your Benched Water Pokémon."

Dark Patch in blue: a [W] Energy card from the discard onto a BENCHED
[W] Pokemon; not offered without both halves.
"""

from spirit.game.attributes import Rarities
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_water_energy_card
from spirit.game.session.effects import is_water_pokemon


def _is_benched_water_pokemon(pokemon):
    # Live types: a Stage 1 made Water by Vaporeon's Aqua Effect qualifies.
    return not is_in_active_spot(pokemon) and is_water_pokemon(pokemon)


def _aqua_patch_condition(board, player_id, pokemon=None):
    bench = board.find_player_area(player_id, "bench")
    if not any(is_water_pokemon(p) for p in (bench.children if bench else [])):
        return False
    discard = board.find_player_area(player_id, "discard")
    return any(is_water_energy_card(c) for c in (discard.children if discard else []))

from spirit.game.data_utils import ItemCardDef

card = ItemCardDef(
    guid="8ac409dc-c7c6-5911-a271-bc58ebadbbe3",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AquaPatch.Name",
    display_name="Aqua Patch",
    searchable_by=["Aqua Patch", "Item", "AquaPatch"],
    subtypes=["Item"],
    collector_number=119,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    effect=attach_from_discard(
        predicate=is_water_energy_card, count=1, minimum=1,
        target=_is_benched_water_pokemon,
        prompt="Choose a Water Energy card to attach to a Benched Water Pokémon"),
    condition=_aqua_patch_condition,
)
