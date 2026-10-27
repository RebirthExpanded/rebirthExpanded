"""Ponyta (SV10 29 -- JP SV9a 013; English DRI/29). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="ff6e56fe-1137-50be-a206-c3db905f4bee",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name",
    display_name="Ponyta",
    searchable_by=["Ponyta", "Basic"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=77,
    abilities=[
        Attack(
            title="Double Headbutt",
            game_text="Flip 2 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=10),
        ),
    ],
)
