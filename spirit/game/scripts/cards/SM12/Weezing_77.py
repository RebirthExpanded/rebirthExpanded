"""Weezing (SM - Cosmic Eclipse 77/236 -- JP SM11b 027/049).

Stage 1 Psychic Pokemon, evolves from Koffing. HP 100, weakness Psychic x2,
retreat 2.

  Ability  Blow-Away Bomb  Once during your turn, when you discard this
                           Pokemon with the effect of Roxie, you may put 1
                           damage counter on each of your opponent's
                           Pokemon. (Place damage counters after the effect
                           of Roxie.)
  Balloon Burst  [PC] 90  Discard this Pokemon and all cards attached to it.

The Ability is Koffing's, word for word, and it works from the HAND -- a
Stage 1 that never has to be played is exactly the point, since Roxie can
throw it away for the counters and the draw.

Balloon Burst discards rather than knocks out, so nobody takes a Prize for
it; emptying the Active spot promotes a new Active afterwards.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.trainers import blow_away_bomb
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers
from spirit.game.session.effects import full_stack


async def balloon_burst(ctx):
    """90, then this Pokemon and everything on it go to the discard."""
    await ctx.deal_damage()
    attacker = ctx.attacker
    if attacker is None:
        return
    was_active = attacker is ctx.my_active()
    await ctx.discard_cards(full_stack(attacker))
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left")
        ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="eee11acc-fbc3-5e54-a246-a082a33e4a73",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weezing.Name",
    display_name="Weezing",
    searchable_by=["Weezing", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=77,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=109,
    abilities=[
        Ability(
            title="Blow-Away Bomb",
            game_text="Once during your turn, when you discard this Pokémon with the effect of Roxie, you may put 1 damage counter on each of your opponent's Pokémon. (Place damage counters after the effect of Roxie.)",
            trigger=Triggers.ON_DISCARDED_BY_ROXIE,
            effect=blow_away_bomb,
        ),
        Attack(
            title="Balloon Burst",
            game_text="Discard this Pokémon and all cards attached to it.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=balloon_burst,
        ),
    ],
)
