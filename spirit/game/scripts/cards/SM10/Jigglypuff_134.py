"""Jigglypuff (ME2 76 -- JP M2 064; English PFL/76). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="e606ae73-463e-5dea-be0d-4772f80d2b5d",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    display_name="Jigglypuff",
    searchable_by=["Jigglypuff", "Basic"],
    subtypes=["Basic"],
    collector_number=134,
    set_code="SM10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=174,
    abilities=[
        Attack(
            title="Ball Roll",
            game_text="Flip a coin until you get tails. This attack does 20 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=ac.flip_damage(until_tails=True, per_heads=20),
        ),
    ],
)
