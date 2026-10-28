"""Magneton (SV3 64 -- JP SVD 037; English OBF/64). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="cef691bb-ebcd-525c-90f5-026049ac90f6",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    display_name="Magneton",
    searchable_by=["Magneton", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    family_id=81,
    abilities=[
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
        ),
        Attack(
            title="Electro Ball",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
