"""Tynamo (SV3 67 -- JP SV3 033; English OBF/67). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="ff62adab-f617-56db-86a0-6a400955a6a7",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name",
    display_name="Tynamo",
    searchable_by=["Tynamo", "Basic"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=602,
    abilities=[
        Attack(
            title="Static Shock",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
        Attack(
            title="Tiny Bolt",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
