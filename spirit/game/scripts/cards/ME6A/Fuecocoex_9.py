"""Fuecoco ex (ME6A 9 -- JP M6a 009; English 30C/147, 30C/15). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="2a4346ec-bd6e-5f97-b443-eb4c35192291",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fuecocoex.Name",
    display_name="Fuecoco ex",
    searchable_by=["Fuecoco ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=9,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=909,
    abilities=[
        Attack(
            title="Singe",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=ac.condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Cheerful Flame",
            game_text="This attack does 70 damage for each Prize card you have taken.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=ac.damage_per(ac.count_prizes_taken("mine"), 70),
        ),
    ],
)
