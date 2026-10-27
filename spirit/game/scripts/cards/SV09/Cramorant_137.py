"""Cramorant (SV09 137 -- JP SVM 119; English JTG/137). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="d46877ea-047f-5fa0-bae1-f7ded8a566b6",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cramorant.Name",
    display_name="Cramorant",
    searchable_by=["Cramorant", "Basic"],
    subtypes=["Basic"],
    collector_number=137,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=845,
    abilities=[
        Attack(
            title="Ceaseless Spitting",
            game_text="Flip a coin until you get tails. This attack does 50 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=ac.flip_damage(until_tails=True, per_heads=50),
        ),
    ],
)
