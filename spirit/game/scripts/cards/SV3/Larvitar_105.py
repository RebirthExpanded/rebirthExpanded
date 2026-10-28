"""Larvitar (SV3 105 -- JP SV3 055; English OBF/105, OBF/203). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="75f24d13-b05e-516f-9189-40e646322a63",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name",
    display_name="Larvitar",
    searchable_by=["Larvitar", "Basic"],
    subtypes=["Basic"],
    collector_number=105,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=246,
    abilities=[
        Attack(
            title="Corkscrew Punch",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Confront",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)
