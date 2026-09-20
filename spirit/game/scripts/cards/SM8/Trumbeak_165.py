"""Trumbeak (SM - Lost Thunder 165/214 -- JP SM8 075/095, the art here).

Stage 1 Colorless Pokemon (evolves from Pikipek). HP 80, weakness
Lightning x2, resistance Fighting -20, retreat 1.

  Mountain Pass  (Ability)  Once during your turn (before your attack), if
                            this Pokemon is in your hand, you may reveal
                            it. If you do, look at the top card of your
                            opponent's deck and put this Pokemon in the
                            Lost Zone. If that card is a Supporter card,
                            you may put it in the Lost Zone. If your
                            opponent has no cards in their deck, you can't
                            use this Ability.
  Peck           [CC] 30

A hand Ability (Pitch a Pyukumuku's shape, usable_from="hand"): the
offer needs a card in the opponent's deck; Garbotoxin reaching the hand
switches it off.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef
from spirit.game.session.effects import is_supporter_card


def _opponent_deck_not_empty(board, player_id, card=None) -> bool:
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    deck = board.find_player_area(opponent, "deck") if opponent else None
    return bool(deck and deck.children)


async def mountain_pass(ctx):
    top = ctx.deck_top(1, player_id=ctx.opponent_id)
    if not top:
        return
    if not await ctx.ask_yes_no(
            "Reveal this Pokémon and put it in the Lost Zone to look at the top card of your opponent's deck?"):
        return
    await ctx.reveal_cards([ctx.source])
    await ctx.session.prompt_view_cards(
        ctx.player_id, ctx.source.entity_id, top,
        prompt="Top card of your opponent's deck")
    await ctx.move_to_lost_zone([ctx.source])
    if is_supporter_card(top[0]) and await ctx.ask_yes_no(
            "Put that Supporter card in your opponent's Lost Zone?"):
        await ctx.reveal_cards(top, to_player=ctx.opponent_id)
        await ctx.move_to_lost_zone(top)


card = PokemonCardDef(
    guid="5c70fde6-3212-5e62-a627-160c812b68c3",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trumbeak.Name",
    display_name="Trumbeak",
    searchable_by=["Trumbeak", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=165,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikipek.Name",
    family_id=731,
    abilities=[
        Ability(
            title="Mountain Pass",
            game_text="Once during your turn (before your attack), if this Pokémon is in your hand, you may reveal it. If you do, look at the top card of your opponent's deck and put this Pokémon in the Lost Zone. If that card is a Supporter card, you may put it in the Lost Zone. If your opponent has no cards in their deck, you can't use this Ability.",
            activation=Activations.ONCE_PER_TURN,
            usable_from="hand",
            condition=_opponent_deck_not_empty,
            effect=mountain_pass,
        ),
        Attack(title="Peck", game_text="", cost={PokemonTypes.COLORLESS: 2}, damage=30),
    ],
)
