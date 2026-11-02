"""Scorbunny (Promo_SWSH 2 -- JP SP 034; English SP/2). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import SpecialConditions


card = PokemonCardDef(
    guid="55a2da61-68cb-5b45-b82c-4854bd21132e",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scorbunny.Name",
    display_name="Scorbunny",
    searchable_by=["Scorbunny", "Basic"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="Promo_SWSH",
    regulation_mark="D",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=813,
    abilities=[
        Attack(
            title="Super Singe",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=ac.condition_attack(SpecialConditions.BURNED, flip=True),
        ),
    ],
)
