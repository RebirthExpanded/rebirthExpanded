"""Rolycoly (SV05 93 -- JP SV5K 039; English TEF/93). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="c1d8c12f-cbf9-5290-b702-c9ab2ced0b84",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rolycoly.Name",
    display_name="Rolycoly",
    searchable_by=["Rolycoly", "Basic"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=837,
    abilities=[
        Attack(
            title="Rolling Tackle",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Power Gem",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
