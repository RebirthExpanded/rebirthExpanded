"""Stunfisk ex (ME2PT5 114 -- JP MC 394; English ASC/114, ASC/252). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="ff29dd5e-f0b8-55c6-ab94-c13b295314d4",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stunfiskex.Name",
    display_name="Stunfisk ex",
    searchable_by=["Stunfisk ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=114,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=618,
    abilities=[
        Attack(
            title="Big Bite",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=ac.condition_attack(no_retreat=True),
        ),
        Attack(
            title="Flopping Trap",
            game_text="If this Pokémon has any damage counters on it, this attack does 100 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=ac.bonus_if(ac.has_damage("self"), 100),
        ),
    ],
)
