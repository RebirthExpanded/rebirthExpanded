"""Spoink (ME1 62 -- JP M1S 044; English MEG/62). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="3e20314d-3066-5125-92d4-75bd7a1abc91",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name",
    display_name="Spoink",
    searchable_by=["Spoink", "Basic"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=325,
    abilities=[
        Attack(
            title="Triple Spin",
            game_text="Flip 3 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=10),
        ),
    ],
)
