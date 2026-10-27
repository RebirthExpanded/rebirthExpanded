"""Simisage (ZSV10PT5 5 -- JP SV11B 005; English BLK/5, BLK/90). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="b68de1aa-57cf-5599-9825-6a5ad0fd8947",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simisage.Name",
    display_name="Simisage",
    searchable_by=["Simisage", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pansage.Name",
    family_id=511,
    abilities=[
        Attack(
            title="Gentle Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
