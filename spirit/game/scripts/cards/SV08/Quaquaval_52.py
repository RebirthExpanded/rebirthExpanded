"""Quaquaval (SV08 52 -- JP SV7a 015; English SSP/52). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

def _up_tempo_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    deck = board.find_player_area(player_id, "deck")
    return bool(hand and hand.children and deck and deck.children)


async def up_tempo(ctx):
    hand = list(ctx.hand())
    if not hand:
        return
    picks = await ctx.choose_cards(hand, 1, minimum=1, prompt="Put a card from your hand on the bottom of your deck")
    if not picks:
        return
    await ctx.put_on_bottom_of_deck(picks[0])
    await ctx.draw_until(5)


card = PokemonCardDef(
    guid="6ef09b79-1726-5815-a1a4-8ca08ea6b3b2",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quaquaval.Name",
    display_name="Quaquaval",
    searchable_by=["Quaquaval", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=52,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quaxwell.Name",
    family_id=912,
    abilities=[
        Ability(
            title="Up-Tempo",
            game_text="You must put a card from your hand on the bottom of your deck in order to use this Ability. Once during your turn, you may draw cards until you have 5 cards in your hand.",
            activation=Activations.ONCE_PER_TURN,
            condition=_up_tempo_condition,
            effect=up_tempo,
        ),
        Attack(
            title="Hydro Splash",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
