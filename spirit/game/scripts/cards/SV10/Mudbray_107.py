"""Mudbray (SV10 107 -- JP SV9a 045; English DRI/107). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="7c1e2c74-3ed7-5df2-96d1-af04e5cddd4f",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mudbray.Name",
    display_name="Mudbray",
    searchable_by=["Mudbray", "Basic"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=749,
    abilities=[
        Attack(
            title="Running Charge",
            game_text="Flip a coin until you get tails. This attack does 40 damage for each heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=ac.flip_damage(until_tails=True, per_heads=40),
        ),
    ],
)
