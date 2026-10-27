"""Melmetal ex (SV07 105 -- JP SVI 041; English SCR/105). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c779218f-19b0-5e9d-a103-4c2aba9c04f1",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Melmetalex.Name",
    display_name="Melmetal ex",
    searchable_by=["Melmetal ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=105,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    family_id=808,
    abilities=[
        Attack(
            title="Iron Swing",
            game_text="Flip 2 coins. This attack does 100 damage for each heads.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=100),
        ),
    ],
)
