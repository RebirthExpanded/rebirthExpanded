"""Pawmo (MEE 4 -- JP MEE 004; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="beed639b-15cc-553a-8bdf-a6bbae34a2da",
    key="MEE",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmo.Name",
    display_name="Pawmo",
    searchable_by=["Pawmo", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="MEE",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmi.Name",
    family_id=921,
    abilities=[
        Attack(
            title="Electro Ball",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=40,
        ),
    ],
)
