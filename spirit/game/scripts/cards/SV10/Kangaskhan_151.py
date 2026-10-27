"""Kangaskhan (SV10 151 -- JP SV10 080; English DRI/151, DRI/204). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="1775b284-523b-50cc-8cc7-afafeacb9fed",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kangaskhan.Name",
    display_name="Kangaskhan",
    searchable_by=["Kangaskhan", "Basic"],
    subtypes=["Basic"],
    collector_number=151,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=115,
    abilities=[
        Attack(
            title="Gentle Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Dizzy Punch",
            game_text="Flip 2 coins. This attack does 90 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=90),
        ),
    ],
)
