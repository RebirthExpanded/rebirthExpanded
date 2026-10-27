"""Gumshoos (ME1 110 -- JP M1L 056; English MEG/110, MEG/153). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

def _evidence_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    deck = board.find_player_area(player_id, "deck")
    return bool(hand and hand.children and deck and deck.children)


async def evidence_gathering(ctx):
    hand = list(ctx.hand())
    top = list(ctx.deck_top(1))
    if not hand or not top:
        return
    picks = await ctx.choose_cards(hand, 1, minimum=1, prompt="Choose a card to switch with the top card of your deck")
    if not picks:
        return
    await ctx.put_in_hand(top, reveal=False)
    await ctx.put_on_top_of_deck(picks[0])


card = PokemonCardDef(
    guid="7dd57988-7c1e-533d-9da4-322592fe069a",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gumshoos.Name",
    display_name="Gumshoos",
    searchable_by=["Gumshoos", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=110,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yungoos.Name",
    family_id=734,
    abilities=[
        Ability(
            title="Evidence Gathering",
            game_text="Once during your turn, you may use this Ability. Switch a card from your hand with the top card of your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_evidence_condition,
            effect=evidence_gathering,
        ),
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
