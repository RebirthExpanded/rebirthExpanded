"""Whirlipede (ZSV10PT5 55 -- JP SV11B 058; English BLK/133, BLK/55). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="77160a2e-b14b-5801-ad4f-52ee8f3a2e63",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whirlipede.Name",
    display_name="Whirlipede",
    searchable_by=["Whirlipede", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Venipede.Name",
    family_id=543,
    abilities=[
        Attack(
            title="Venoshock",
            game_text="If your opponent's Active Pokémon is Poisoned, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(ac.defender_has_condition(SpecialConditions.POISONED), 60),
        ),
    ],
)
