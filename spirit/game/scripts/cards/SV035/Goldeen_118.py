"""Goldeen (SV035 118 -- JP SV2a 118; English MEW/118). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="ef900725-1cc1-50da-b1ca-8f3aca45baac",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Goldeen.Name",
    display_name="Goldeen",
    searchable_by=["Goldeen", "Basic"],
    subtypes=["Basic"],
    collector_number=118,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=118,
    abilities=[
        Attack(
            title="Triple Strike",
            game_text="Flip 3 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=10),
        ),
        Attack(
            title="Sprinkle Water",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
