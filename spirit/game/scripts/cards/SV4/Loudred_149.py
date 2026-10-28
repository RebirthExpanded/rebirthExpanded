"""Loudred (SV4 149 -- JP SV4K 056; English PAR/149, PAR/212). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="721f0a45-08ef-579b-947a-0635c2277852",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Loudred.Name",
    display_name="Loudred",
    searchable_by=["Loudred", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=149,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Whismur.Name",
    family_id=293,
    abilities=[
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Mega Impact",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
