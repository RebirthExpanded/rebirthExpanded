"""Crocalor (SV1 37 -- JP SVAL 003; English SVI/37). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="ed600712-5a74-5e20-af15-cb24b9930092",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crocalor.Name",
    display_name="Crocalor",
    searchable_by=["Crocalor", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fuecoco.Name",
    family_id=909,
    abilities=[
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Rolling Tackle",
            game_text="",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
