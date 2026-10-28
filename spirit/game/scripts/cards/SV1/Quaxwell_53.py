"""Quaxwell (SV1 53 -- JP SVAW 003; English SVI/53). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="226b7d90-8072-5fac-9769-7690310aea90",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quaxwell.Name",
    display_name="Quaxwell",
    searchable_by=["Quaxwell", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quaxly.Name",
    family_id=912,
    abilities=[
        Attack(
            title="Rain Splash",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Spiral Kick",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
