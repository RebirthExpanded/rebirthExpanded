"""Flittle (SV4 79 -- JP SV4M 031; English PAR/79). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5fc666c8-485a-5383-b76f-a6a676d07ab1",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name",
    display_name="Flittle",
    searchable_by=["Flittle", "Basic"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=955,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="+",
            effect=ac.flip_bonus(20),
        ),
    ],
)
