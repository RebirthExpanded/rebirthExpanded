"""Gimmighoul (SV4 88 -- JP SV3a 021; English PAR/198, PAR/88). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="6d7d8916-afe2-5f8c-8398-9f425151f152",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gimmighoul.Name",
    display_name="Gimmighoul",
    searchable_by=["Gimmighoul", "Basic"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=999,
    abilities=[
        Attack(
            title="Continuous Coin Toss",
            game_text="Flip a coin until you get tails. This attack does 20 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=ac.flip_damage(until_tails=True, per_heads=20),
        ),
    ],
)
