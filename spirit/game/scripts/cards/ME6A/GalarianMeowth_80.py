"""Galarian Meowth (ME6A 80 -- JP M6a 080; English 30C/101, 30C/141). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="f6254408-ecd1-566f-8d96-017cb9a0fe7b",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMeowth.Name",
    display_name="Galarian Meowth",
    searchable_by=["Galarian Meowth", "Basic"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=52,
    abilities=[
        Attack(
            title="Pay Day",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=su.draw_attack(1),
        ),
        Attack(
            title="Treasure Rush",
            game_text="This attack does 10 damage for each card in your hand.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            damage_operator="x",
            effect=ac.damage_per(ac.count_hand("mine"), 10),
        ),
    ],
)
