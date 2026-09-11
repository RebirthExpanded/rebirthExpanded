"""Palafin (SV - Twilight Masquerade 60/167 -- JP SV6 035/101).

Stage 1 Water Pokemon, evolves from Finizen. HP 100, weakness Lightning
x2, retreat 1.

  Ability  Zero to Hero  Once during your turn, when this Pokemon moves
                         from the Active Spot to the Bench, you may search
                         your deck for a Palafin ex and switch it with this
                         Pokemon. Any attached cards, damage counters,
                         Special Conditions, turns in play, and any other
                         effects remain on the new Pokemon. If you switched
                         a Pokemon in this way, put this card into your
                         deck. Then, shuffle your deck.
  Wave Splash  [WC] 30

Rides ON_MOVE_TO_BENCH (a retreat or a switch during the owner's turn;
an opponent's gust is not "your turn"); the swap is the identity_swap
primitive with the deck as the outgoing card's destination.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import (Ability, Attack, PokemonCardDef,
                                    Triggers, def_for)


def _is_palafin_ex(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", "") == "Palafin ex"


def _zero_to_hero_condition(board, player_id, pokemon=None) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def zero_to_hero(ctx):
    if not await ctx.ask_yes_no(
            "Search your deck for a Palafin ex and switch it with this Pokémon?"):
        return
    picks = await ctx.search_deck(
        _is_palafin_ex, count=1, minimum=0,
        prompt="Choose a Palafin ex to switch with this Pokémon.")
    if picks:
        await ctx.identity_swap(ctx.source, picks[0], destination="deck")
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="bb1bd945-d25a-5123-8a17-efa33e90f049",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palafin.Name",
    display_name="Palafin",
    searchable_by=["Palafin", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="SV06",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name",
    family_id=963,
    regulation_mark="H",
    abilities=[
        Ability(
            title="Zero to Hero",
            game_text="Once during your turn, when this Pokémon moves from the Active Spot to the Bench, you may search your deck for a Palafin ex and switch it with this Pokémon. Any attached cards, damage counters, Special Conditions, turns in play, and any other effects remain on the new Pokémon. If you switched a Pokémon in this way, put this card into your deck. Then, shuffle your deck.",
            trigger=Triggers.ON_MOVE_TO_BENCH,
            condition=_zero_to_hero_condition,
            effect=zero_to_hero,
        ),
        Attack(title="Wave Splash", game_text="",
               cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=30),
    ],
)
