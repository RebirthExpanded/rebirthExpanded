"""Hakamo-o (ME6A 90 -- JP M6a 090; English 30C/111). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="e20ef98a-2d4c-565d-9e21-a318d8a43aa4",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hakamoo.Name",
    display_name="Hakamo-o",
    searchable_by=["Hakamo-o", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=90,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jangmoo.Name",
    family_id=782,
    abilities=[
        Attack(
            title="Sharp Fang",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Dragon Claw",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            damage=70,
        ),
    ],
)
