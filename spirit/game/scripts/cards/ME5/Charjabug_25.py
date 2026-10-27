"""Charjabug (ME5 25 -- JP M5 024; English PBL/25). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="8c064a0b-8918-53e5-8322-96eb77aeef43",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name",
    display_name="Charjabug",
    searchable_by=["Charjabug", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grubbin.Name",
    family_id=736,
    abilities=[
        Attack(
            title="Vise Grip",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
        ),
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=50,
        ),
    ],
)
