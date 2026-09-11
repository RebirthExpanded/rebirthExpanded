"""Scatterbug (SM - Forbidden Light 5/131 -- JP SM6 004/094).

Basic Grass Pokemon. HP 30, weakness Fire x2, retreat 1.

  Ability  Abnormal Outbreak  You can use this Ability only if you go
                              second. Once during your first turn (before
                              your attack), you may search your deck for a
                              Spewpa and a Vivillon, reveal them, and put
                              them into your hand. Then, shuffle your deck.
  Tackle  [CC] 10

"Only if you go second, during your first turn" is turn 2 of the game, the
same reading Shaymin (ASR 14) takes. Both halves of the line come out at
once through one browser with two labeled slots, and either slot may come
up empty.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef, def_for)


def _named(name):
    def _pred(card):
        definition = def_for(card.archetype_id)
        return bool(definition) and definition.display_name == name
    return _pred


def _second_players_first_turn(board, player_id, pokemon) -> bool:
    return board.turn_state.turn_number == 2


async def abnormal_outbreak(ctx):
    """A Spewpa and a Vivillon out of the deck, in one browser."""
    spewpa, vivillon = await ctx.search_deck_groups(
        [(_named("Spewpa"), 1, "Spewpa"),
         (_named("Vivillon"), 1, "Vivillon")],
        prompt="Choose a Spewpa and a Vivillon.",
    )
    picks = list(spewpa) + list(vivillon)
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="b158b1e4-dd09-5134-b9ff-346a282ac45d",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scatterbug.Name",
    display_name="Scatterbug",
    searchable_by=["Scatterbug", "Basic"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=664,
    abilities=[
        Ability(
            title="Abnormal Outbreak",
            game_text="You can use this Ability only if you go second. Once during your first turn (before your attack), you may search your deck for a Spewpa and a Vivillon, reveal them, and put them into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_second_players_first_turn,
            effect=abnormal_outbreak,
        ),
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
        ),
    ],
)
