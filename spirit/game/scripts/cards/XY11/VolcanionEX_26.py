"""Volcanion-EX (XY - Steam Siege 26/114 -- JP XY11-Bb 012/054).

Basic Fire AND Water Pokemon-EX -- the pool's first dual-type card. HP 180,
weakness Water x2, retreat 3.

  Ability  Steam Up  Once during your turn (before your attack), you may
                     discard a [R] Energy card from your hand. If you do,
                     during this turn, your Basic [R] Pokemon's attacks do
                     30 more damage to your opponent's Active Pokemon
                     (before applying Weakness and Resistance).
  Volcanic Heat  [RRC] 130  This Pokemon can't attack during your next
                            turn.

Both types sit in POKEMON_TYPES, so the deck builder's type filter finds
it under Fire and under Water, Weakness/Resistance and every "[R] / [W]
Pokemon" predicate see both, and the type words are search aliases too.
Steam Up is a turn damage modifier keyed on the attacker being a Basic
[R] Pokemon (live types); several uses stack, and Volcanion-EX itself
qualifies.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.card_effects.trainers import is_fire_energy_card
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)
from spirit.game.session.effects import (is_basic_pokemon_in_play,
                                         is_pokemon_of_type)
from spirit.game.session.passives import TurnDamageModifier


def _basic_fire_pokemon(pokemon) -> bool:
    return is_basic_pokemon_in_play(pokemon) and \
        is_pokemon_of_type(pokemon, PokemonTypes.FIRE)


async def steam_up(ctx):
    paid = await ctx.discard_from_hand(
        1, predicate=is_fire_energy_card,
        prompt="Discard a Fire Energy card for Steam Up")
    if not paid:
        return
    ctx.add_turn_damage_modifier(TurnDamageModifier(
        30, ctx.player_id, opposing_active_only=True,
        source_predicate=_basic_fire_pokemon))
    for pokemon in ctx.my_pokemon_in_play():
        if _basic_fire_pokemon(pokemon):
            await ctx.add_stat_visualization(
                pokemon, "Positive", "DamageDealtIncreased", card_text="+30 damage")


card = PokemonCardDef(
    guid="79a16bae-9f9c-58c8-a35c-430f6ceee34b",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VolcanionEX.Name",
    display_name="Volcanion-EX",
    searchable_by=["Volcanion-EX", "Basic", "EX", "VolcanionEX", "Fire", "Water"],
    subtypes=["Basic", "EX"],
    collector_number=26,
    set_code="XY11",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIRE, PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=721,
    abilities=[
        Ability(
            title="Steam Up",
            game_text="Once during your turn (before your attack), you may discard a [R] Energy card from your hand. If you do, during this turn, your Basic [R] Pokémon's attacks do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_hand(is_fire_energy_card, 1),
            effect=steam_up,
        ),
        Attack(
            title="Volcanic Heat",
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            locks_next_turn=True,
        ),
    ],
)
