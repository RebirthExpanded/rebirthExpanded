"""Drizzile (ME1 40 -- JP M1S 022; English MEG/40). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="fc270c00-8139-59c3-9ead-a5db8ce5e39c",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drizzile.Name",
    display_name="Drizzile",
    searchable_by=["Drizzile", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sobble.Name",
    family_id=816,
    abilities=[
        Attack(
            title="Double Stab",
            game_text="Flip 2 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=30),
        ),
    ],
)
