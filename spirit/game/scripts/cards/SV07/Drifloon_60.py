"""Drifloon (SV07 60 -- JP SV7 040; English SCR/60). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="41fd8949-75a8-5636-b487-ee45dbd8df85",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    display_name="Drifloon",
    searchable_by=["Drifloon", "Basic"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=425,
    abilities=[
        Attack(
            title="Expand",
            game_text="During your opponent's next turn, this Pokémon takes 10 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=pc.protect_next_turn(reduce=10),
        ),
    ],
)
