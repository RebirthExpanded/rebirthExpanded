"""Pokemon Research Lab (SM - Unified Minds 205/236 -- JP SM11 089/094).

Stadium.

  "Once during each player's turn, that player may search their deck for
   up to 2 Pokemon that evolve from Unidentified Fossil, put those Pokemon
   onto their Bench, and shuffle their deck. If a player searches their
   deck in this way, their turn ends."

The Bench cap limits the take; searching at all (even finding nothing)
ends the turn. Not offered with a full Bench or an empty deck.
"""

from spirit.game.attributes import AttrID, Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.data_utils import Ability, Activations, StadiumCardDef
from spirit.game.session.effects import is_pokemon_card
from spirit.game.session.passives import effective_bench_capacity


def _evolves_from_fossil(card) -> bool:
    return is_pokemon_card(card) and \
        card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == "UnidentifiedFossil"


def _lab_condition(board, player_id, pokemon=None) -> bool:
    deck = board.find_player_area(player_id, "deck")
    bench = board.find_player_area(player_id, "bench")
    return bool(deck and deck.children) and \
        len(bench.children if bench else []) < effective_bench_capacity(board, player_id)


async def pokemon_research_lab(ctx):
    await search_to_bench(
        predicate=_evolves_from_fossil, count=2,
        prompt="Choose up to 2 Pokémon that evolve from Unidentified Fossil.")(ctx)
    ctx.ends_turn = True


ABILITY = Ability(
    title="Pokémon Research Lab",
    game_text="Once during each player's turn, that player may search their deck for up to 2 Pokémon that evolve from Unidentified Fossil, put those Pokémon onto their Bench, and shuffle their deck. If a player searches their deck in this way, their turn ends.",
    activation=Activations.ONCE_PER_TURN,
    condition=_lab_condition,
    effect=pokemon_research_lab,
)

card = StadiumCardDef(
    guid="6443d408-7c41-5b79-82a0-efcc260f3ec3",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonResearchLab.Name",
    display_name="Pokémon Research Lab",
    searchable_by=["Pokémon Research Lab", "Stadium", "PokemonResearchLab"],
    subtypes=["Stadium"],
    collector_number=205,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    ability=ABILITY,
)
