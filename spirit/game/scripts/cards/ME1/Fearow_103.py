"""Fearow (ME1 103 -- JP M1L 053; English MEG/103). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="b807b09b-9af6-5dfc-ba53-9c14ce4c2377",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fearow.Name",
    display_name="Fearow",
    searchable_by=["Fearow", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=103,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name",
    family_id=21,
    abilities=[
        Attack(
            title="Repeating Drill",
            game_text="Flip 5 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=ac.flip_damage(coins=5, per_heads=30),
        ),
    ],
)
