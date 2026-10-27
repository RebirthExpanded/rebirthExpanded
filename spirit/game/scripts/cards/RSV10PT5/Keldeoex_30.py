"""Keldeo ex (RSV10PT5 30 -- JP SV11W 027; English WHT/159, WHT/167, WHT/30). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _entered_active_this_turn(ctx) -> bool:
    return ctx.entered_active_this_turn(ctx.attacker)


card = PokemonCardDef(
    guid="ab48edae-a73b-5dea-9c36-18db03011d39",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Keldeoex.Name",
    display_name="Keldeo ex",
    searchable_by=["Keldeo ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=30,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=647,
    abilities=[
        Attack(
            title="Gale Thrust",
            game_text="If this Pokémon moved from your Bench to the Active Spot this turn, this attack does 90 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_entered_active_this_turn, 90),
        ),
        Attack(
            title="Sonic Edge",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=ac.ignore_effects_attack(),
        ),
    ],
)
