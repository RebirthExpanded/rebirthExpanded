"""Nacli (SV4 102 -- JP SV4K 038; English PAR/102). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="61d60bda-7db0-54c1-9922-fd59040719df",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nacli.Name",
    display_name="Nacli",
    searchable_by=["Nacli", "Basic"],
    subtypes=["Basic"],
    collector_number=102,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=932,
    abilities=[
        Attack(
            title="Corner",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=ac.condition_attack(no_retreat=True),
        ),
    ],
)
