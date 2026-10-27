"""Krokorok (ME2 65 -- JP M2 054; English PFL/65). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="6189dce9-befe-5f56-93b6-333c19ae1f76",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    display_name="Krokorok",
    searchable_by=["Krokorok", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=65,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandile.Name",
    family_id=551,
    abilities=[
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
        ),
        Attack(
            title="Confront",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
