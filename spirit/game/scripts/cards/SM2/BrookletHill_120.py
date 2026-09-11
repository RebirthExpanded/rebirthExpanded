"""Brooklet Hill (SM - Guardians Rising 120/145 -- JP SM6a 050/053).

Stadium.

  "Once during each player's turn, that player may search their deck for a Basic Water Pokémon or Basic Fighting Pokémon, put it onto their Bench, and shuffle their deck."

Straight onto the Bench, not into the hand -- so no on-play trigger
fires, and the ability is not offered with a full Bench.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import (requires_bench_space,
                                                      search_to_bench)
from spirit.game.card_effects.trainers import is_basic_water_or_fighting_pokemon
from spirit.game.data_utils import Ability, Activations, StadiumCardDef

ABILITY = Ability(
    title="Brooklet Hill",
    game_text="Once during each player's turn, that player may search their deck for a Basic Water Pokémon or Basic Fighting Pokémon, put it onto their Bench, and shuffle their deck.",
    activation=Activations.ONCE_PER_TURN,
    effect=search_to_bench(
        is_basic_water_or_fighting_pokemon, count=1,
        prompt="Choose a Basic Water or Fighting Pokémon to put onto your Bench."),
    condition=requires_bench_space(1),
)

card = StadiumCardDef(
    guid="107917c1-d3b3-5e48-bea0-8c8d2166d177",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrookletHill.Name",
    display_name="Brooklet Hill",
    searchable_by=["Brooklet Hill", "Stadium", "BrookletHill"],
    subtypes=["Stadium"],
    collector_number=120,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    ability=ABILITY,
)
