"""Eelektross (ZSV10PT5 32 -- JP SV11B 035; English BLK/115, BLK/32). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="560e0e61-c552-5adb-ac54-1eb4fb6a51f5",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektross.Name",
    display_name="Eelektross",
    searchable_by=["Eelektross", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=32,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name",
    family_id=602,
    abilities=[
        Attack(
            title="Thunder Fang",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=60,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Buzz Flip",
            game_text="Flip 4 coins. This attack does 100 damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="x",
            effect=ac.flip_damage(coins=4, per_heads=100),
        ),
    ],
)
