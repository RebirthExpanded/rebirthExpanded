"""Heracross (SM - Unified Minds 107/236 -- JP SM11 046/094, the art here).

Basic Fighting Pokemon. HP 100, weakness Psychic x2, retreat 1.

  Turn the Tables [C]   If 1 of your opponent's Pokemon used a GX attack
                        during their last turn, your opponent shuffles their
                        Active Pokemon and all cards attached to it into
                        their deck.
  Tackle          [CCC] 70

"Used a GX attack" reads TurnState.gx_attack_users_last_turn, which a GX
attack reached through a copy (Copycat into Apex Dragon into a GX attack)
also marks -- the attack ledger only records the declared title.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import full_stack


def _they_used_gx_last_turn(ctx) -> bool:
    return ctx.opponent_id in ctx.session.turn_state.gx_attack_users_last_turn


async def turn_the_tables(ctx):
    target = ctx.defender
    if target is None or not _they_used_gx_last_turn(ctx) or ctx.effects_blocked(target):
        return
    await ctx.shuffle_into_deck(full_stack(target), player_id=ctx.opponent_id)

    async def _promote():
        if ctx.board.active_pokemon(ctx.opponent_id) is None \
                and not await ctx.session._promote_new_active(ctx.opponent_id):
            screen_name = ctx.session.players[ctx.opponent_id].screen_name
            await ctx.session.end_game(ctx.player_id, f"{screen_name} has no Pokémon left")
    ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="01b4b0d9-3b05-58e4-af45-39d5ea009f7a",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heracross.Name",
    display_name="Heracross",
    searchable_by=["Heracross", "Basic"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=214,
    abilities=[
        Attack(
            title="Turn the Tables",
            game_text="If 1 of your opponent's Pokémon used a GX attack during their last turn, your opponent shuffles their Active Pokémon and all cards attached to it into their deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=turn_the_tables,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)
