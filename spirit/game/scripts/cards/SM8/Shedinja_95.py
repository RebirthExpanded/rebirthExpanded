"""Shedinja (SM - Lost Thunder 95/214 -- JP SM7b 015/050, the art here).

Stage 1 Psychic Pokemon (evolves from Nincada). HP 40, no weakness, no
resistance, retreat 1.

  Vessel of Life  (Ability)  Once during your turn (before your attack), you
                             may discard all cards attached to this Pokemon
                             and attach it to 1 of your Pokemon as a Pokemon
                             Tool card. When the Pokemon this card is
                             attached to is Knocked Out, your opponent takes
                             1 fewer Prize card.
  Haunt  [C]  Put 3 damage counters on your opponent's Active Pokemon.

Klefki's Wonder Lock is the precedent: the card ITSELF becomes the Tool
(ctx.attach_as_tool), so a Tool lock (Jamming Tower, Ancient Custom)
switches the Prize text off but does not stop the attach, Tool counters
(Tool Drop, Pumpkin Bomb) see it, and nothing counts it as a Pokemon in
play (Midrumble, G-Max Fall, Line Force, Riotous Beating). Official Q&A:

- It may be used from the Active Spot too; the player then promotes.
- The Nincada under an evolved Shedinja is discarded with the rest.
- Each Shedinja takes one Prize off: two on Genesect-GX leave nothing to
  take. Prize-adding attacks still add on top (Gluttony-GX takes 2).
- With Legacy Energy on the same 1-Prize Pokemon nothing is taken, and
  Legacy Energy's once-per-game effect counts as used.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import place_counters
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef
from spirit.game.session.passives import Passive, carrier_pokemon, tool_slots_free


class _VesselOfLifePassive(Passive):
    """Only as a Tool, and only for the Pokemon it is attached to."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if not getattr(carrier, "acts_as_tool", False) \
                or carrier_pokemon(carrier) is not pokemon:
            return count
        return max(0, count - 1)


def _holders(board, player_id, shedinja):
    return [p for p in board.pokemon_in_play(player_id)
            if p is not shedinja and tool_slots_free(board, p) > 0]


def _has_a_holder(board, player_id, pokemon) -> bool:
    return bool(_holders(board, player_id, pokemon))


async def vessel_of_life(ctx):
    shedinja = ctx.source
    candidates = _holders(ctx.board, ctx.player_id, shedinja)
    if not candidates:
        return
    holder = await ctx.choose_pokemon(
        candidates, "Choose a Pokémon to attach Shedinja to as a Pokémon Tool")
    if holder is None:
        return
    was_active = ctx.board.active_pokemon(ctx.player_id) is shedinja
    # Energy, Tools and the Nincada it evolved from all go to the discard.
    attached = list(shedinja.children)
    if attached:
        await ctx.discard_cards(attached)
    if not await ctx.attach_as_tool(shedinja, holder):
        return
    if was_active:
        # After the attach choreography flushes, as Psychic Leap does.
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left")

        ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="d0423f67-729d-57bd-b2b0-35447844e6dd",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shedinja.Name",
    display_name="Shedinja",
    searchable_by=["Shedinja", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=95,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    passive=_VesselOfLifePassive(),
    abilities=[
        Ability(
            title="Vessel of Life",
            game_text="Once during your turn (before your attack), you may discard all cards attached to this Pokémon and attach it to 1 of your Pokémon as a Pokémon Tool card. When the Pokémon this card is attached to is Knocked Out, your opponent takes 1 fewer Prize card.",
            activation=Activations.ONCE_PER_TURN,
            condition=_has_a_holder,
            effect=vessel_of_life,
        ),
        Attack(
            title="Haunt",
            game_text="Put 3 damage counters on your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=place_counters(3),
        ),
    ],
)
