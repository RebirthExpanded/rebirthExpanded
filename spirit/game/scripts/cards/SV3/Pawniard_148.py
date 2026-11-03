"""Pawniard (SV3 148 -- JP SV3 080; English OBF/148). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="74a40b76-9b78-584d-909a-efc30365c17d",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name",
    display_name="Pawniard",
    searchable_by=["Pawniard", "Basic"],
    subtypes=["Basic"],
    collector_number=148,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=624,
    abilities=[
        Attack(
            title="Triple Cutter",
            game_text="Flip 3 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            damage_operator="x",
            effect=ac.flip_damage(3, per_heads=10),
        ),
    ],
)
