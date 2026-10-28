"""Dugtrio (SV035 51 -- JP SV2a 051; English MEW/51). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="78700ff4-562f-5c0e-9190-3bec3d238f0f",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dugtrio.Name",
    display_name="Dugtrio",
    searchable_by=["Dugtrio", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name",
    family_id=50,
    abilities=[
        Attack(
            title="Headbutt Bounce",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
        Attack(
            title="Mud Bomb",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2},
            damage=80,
        ),
    ],
)
