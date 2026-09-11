"""Milotic (XY - Flashfire 23/106 -- JP XY2 010/080).

Stage 1 Water Pokemon, evolves from Feebas. HP 100, weakness Grass x2,
retreat 2.

  Ability  Energy Grace  Once during your turn (before your attack), you may
                         Knock Out this Pokemon. If you do, attach 3 basic
                         Energy cards from your discard pile to 1 of your
                         Pokemon (excluding Pokemon-EX).
  Waterfall  [WCC] 60

BANNED in Expanded (pokemon.com's list: 23/106), and formats.json already
names it; implemented so the card exists, not so it can be played.

The knockout is the price and it is paid first -- the opponent takes a
Prize -- and the Energy then lands on one of your other Pokemon (it can
hardly land on this one). "Excluding Pokemon-EX" is the uppercase XY rule
box; a Scarlet & Violet ex is not excluded.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import requires_discard
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef, subtypes_for)
from spirit.game.session.effects import EffectContext, is_basic_energy


def _not_uppercase_ex(pokemon) -> bool:
    return "EX" not in subtypes_for(pokemon.archetype_id)


def _energy_grace_condition(board, player_id, pokemon) -> bool:
    """Something to attach and somewhere to attach it (the Milotic itself
    will be in the discard pile by then)."""
    if not requires_discard(is_basic_energy, 1)(board, player_id):
        return False
    return any(p is not pokemon and _not_uppercase_ex(p)
               for p in board.pokemon_in_play(player_id))


async def energy_grace(ctx):
    """Faint on purpose; then 3 basic Energy from the discard onto a non-EX."""
    if not await ctx.ask_yes_no(
            "Knock Out this Pokémon to attach 3 basic Energy cards from your "
            "discard pile to 1 of your Pokémon?"):
        return
    if not await ctx.knock_out(ctx.source):
        return
    session, player_id, source = ctx.session, ctx.player_id, ctx.source

    # The KO (and its Prize) resolves first; the attach then runs on a fresh
    # context so its choreography flushes as its own bracket -- the way
    # resolve_knockouts runs the Energy leave-play hooks.
    async def _attach():
        hook_ctx = EffectContext(session, player_id, source, None)
        targets = [p for p in hook_ctx.my_pokemon_in_play() if _not_uppercase_ex(p)]
        energies = [c for c in hook_ctx.discard_pile() if is_basic_energy(c)]
        if not targets or not energies:
            return
        target = await hook_ctx.choose_pokemon(
            targets, "Choose a Pokémon to attach the Energy to")
        if target is None:
            return
        picks = await hook_ctx.choose_cards(
            energies, 3, minimum=min(3, len(energies)),
            prompt="Choose 3 basic Energy cards to attach.")
        for energy in picks:
            await hook_ctx.attach_energy(energy, target)
        await hook_ctx.flush_choreography()
        for hook in hook_ctx.deferred_actions:
            await hook()

    ctx.deferred_actions.append(_attach)


card = PokemonCardDef(
    guid="17063f5b-808e-5f8f-87a8-f9515047f2b3",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Milotic.Name",
    display_name="Milotic",
    searchable_by=["Milotic", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    family_id=349,
    abilities=[
        Ability(
            title="Energy Grace",
            game_text="Once during your turn (before your attack), you may Knock Out this Pokémon. If you do, attach 3 basic Energy cards from your discard pile to 1 of your Pokémon (excluding Pokémon-EX).",
            activation=Activations.ONCE_PER_TURN,
            condition=_energy_grace_condition,
            effect=energy_grace,
        ),
        Attack(title="Waterfall", game_text="",
               cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2}, damage=60),
    ],
)
