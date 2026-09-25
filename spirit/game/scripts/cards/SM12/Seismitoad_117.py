"""Seismitoad (SM - Cosmic Eclipse 117/236 -- JP SM11b 033/049).

Stage 2 Fighting Pokemon, evolves from Palpitoad. HP 160, weakness Grass
x2, retreat 3.

  Ability  Bulldoze  Once during your turn (before your attack), you may
                     search your deck for a card, shuffle your deck, then put
                     that card on top of it.
  Tremulous Fist  [FCCC] 80+  This attack does 30 more damage for each of
                              your Benched Pokemon that has any damage
                              counters on it.

Bulldoze is Magcargo (CES)'s Smooth Over.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_bench, damage_per
from spirit.game.session.passives import effective_max_hp
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef


def _deck_not_empty(board, player_id, pokemon) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def bulldoze(ctx):
    picks = await ctx.search_deck(None, count=1, minimum=0,
                                  prompt="Choose a card to put on top of your deck")
    await ctx.shuffle_deck()
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


def _damaged(ctx):
    return lambda p: p.get_attribute(AttrID.HP, 0) < effective_max_hp(ctx.board, p)


def _damaged_bench(ctx) -> int:
    return count_bench("mine", _damaged(ctx))(ctx)


card = PokemonCardDef(
    guid="09b94778-b020-5c7b-ba15-584b145f9a60",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seismitoad.Name",
    display_name="Seismitoad",
    searchable_by=['Seismitoad', 'Stage 2', 'Seismitoad'],
    subtypes=['Stage 2'],
    collector_number=117,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    family_id=535,
    abilities=[
        Ability(
            title="Bulldoze",
            game_text="Once during your turn (before your attack), you may search your deck for a card, shuffle your deck, then put that card on top of it.",
            activation=Activations.ONCE_PER_TURN,
            condition=_deck_not_empty,
            effect=bulldoze,
        ),
        Attack(title="Tremulous Fist", game_text="This attack does 30 more damage for each of your Benched Pokémon that has any damage counters on it.",
               cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3}, damage=80, damage_operator="+",
               effect=damage_per(_damaged_bench, 30, base=80)),
    ],
)
