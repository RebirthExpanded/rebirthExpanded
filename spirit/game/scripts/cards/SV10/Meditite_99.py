"""Meditite (SV10 99 -- JP SV10 053; English DRI/99). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="321b4b5f-a073-5e47-b2f6-4a607e9858b5",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    display_name="Meditite",
    searchable_by=["Meditite", "Basic"],
    subtypes=["Basic"],
    collector_number=99,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=307,
    abilities=[
        Attack(
            title="Steady Punch",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="+",
            effect=ac.flip_bonus(20),
        ),
    ],
)
