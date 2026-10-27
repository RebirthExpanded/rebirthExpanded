"""Sprigatito (SV09 16 -- JP SV9 010; English JTG/16). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="3658fcf2-f572-5285-97dd-6f2943167a80",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sprigatito.Name",
    display_name="Sprigatito",
    searchable_by=["Sprigatito", "Basic"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=906,
    abilities=[
        Attack(
            title="Tons of Treading",
            game_text="Flip 3 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=10),
        ),
    ],
)
