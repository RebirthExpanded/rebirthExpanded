"""Gothitelle (SV2 92 -- JP SV2P 033; English PAL/92). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _read_condition(board, player_id, pokemon) -> bool:
    other = next((pid for pid in board.player_ids if pid != player_id), None)
    deck = board.find_player_area(other, "deck") if other else None
    return bool(deck and len(deck.children) >= 1)


async def read_the_stars(ctx):
    top = list(ctx.deck_top(2, player_id=ctx.opponent_id))
    if not top:
        return
    await ctx.reveal_cards(top, to_player=ctx.player_id)
    if len(top) < 2:
        return
    keep = await ctx.choose_cards(top, 1, minimum=1, prompt="Choose the card to put back on top")
    for card in top:
        if keep and card is not keep[0]:
            await ctx.put_on_bottom_of_deck(card)


async def psych_out(ctx):
    await ctx.deal_damage()
    await ac.discard_random_from_hand(ctx, ctx.opponent_id, count=1)


card = PokemonCardDef(
    guid="6f341771-29d2-5fc6-aaf8-bc9b3a57b1dd",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothitelle.Name",
    display_name="Gothitelle",
    searchable_by=["Gothitelle", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=92,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name",
    family_id=574,
    abilities=[
        Ability(
            title="Read the Stars",
            game_text="Once during your turn, you may look at the top 2 cards of your opponent's deck and put 1 of them back. Put the other card on the bottom of their deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_read_condition,
            effect=read_the_stars,
        ),
        Attack(
            title="Psych Out",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=psych_out,
        ),
    ],
)
