"""Medicham (SV07 79 -- JP SVI 030; English SCR/79). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="45ddd55e-edf3-5164-90b6-6480590b7a48",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Medicham.Name",
    display_name="Medicham",
    searchable_by=["Medicham", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    family_id=307,
    abilities=[
        Attack(
            title="Double Smash",
            game_text="Flip 2 coins. This attack does 40 damage for each heads.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=40),
        ),
    ],
)
