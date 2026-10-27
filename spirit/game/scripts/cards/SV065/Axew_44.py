"""Axew (SV065 44 -- JP SV6a 044; English SFA/44). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="4abee9bf-d976-5d92-b3f9-b96542bed856",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Axew.Name",
    display_name="Axew",
    searchable_by=["Axew", "Basic"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=610,
    abilities=[
        Attack(
            title="Scratch",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Sharp Fang",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            damage=30,
        ),
    ],
)
