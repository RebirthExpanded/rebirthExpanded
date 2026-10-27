"""Vanillish (RSV10PT5 28 -- JP SV11W 025; English WHT/112, WHT/28). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="46f35ea9-60d1-54ee-b92a-eb5abce1eb11",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name",
    display_name="Vanillish",
    searchable_by=["Vanillish", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillite.Name",
    family_id=582,
    abilities=[
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Ice Beam",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
