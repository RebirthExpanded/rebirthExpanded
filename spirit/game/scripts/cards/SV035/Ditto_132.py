"""Ditto (SV - 151 132/165 -- JP SV2a 132/165).

Basic Colorless. HP 60, weakness Fighting x2, retreat 1, regulation
mark G.

  Ability  Transformative Start  Once during your first turn, if this
                                 Pokemon is in the Active Spot, you may
                                 search your deck and choose a Basic Pokemon
                                 you find there, except any Ditto. Discard
                                 this Pokemon and all attached cards, and
                                 put that Basic Pokemon in this Pokemon's
                                 place. Then, shuffle your deck.

A start-of-game trick, so the conditions are all about timing: the Active
Spot, and your FIRST turn -- turn 1 for the player going first and turn 2
for the other, which is what "your first turn" means to the turn counter.
After that the Ability is simply not offered.

The replacement is not a switch and not a bench play: it is the identity
swap Zoroark's Phantom Transformation already uses, with the deck as the
source instead of the discard pile. transfer=False is the difference that
matters -- Ditto's attachments go to the discard with it rather than
following the new Pokemon, which is what "discard this Pokemon and all
attached cards" says. No on-play trigger fires; the new Active is simply
there.

"Except any Ditto" is by name, so this printing cannot fetch the Pokemon GO
one either.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)
from spirit.game.session.effects import is_basic_pokemon

DITTO_NAME = "com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name"


def _is_other_basic(card) -> bool:
    """"except any Ditto" is by name, so the short logic name decides -- the
    NAME attribute is a localisation dict, not a string to compare."""
    return (is_basic_pokemon(card)
            and card.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) != "Ditto")


def _transformative_start_condition(board, player_id, pokemon=None):
    """Active spot, and it is still this player's first turn."""
    state = getattr(board, "turn_state", None)
    turn = getattr(state, "turn_number", 99) if state is not None else 99
    if turn > 2:
        return False
    return pokemon is not None and board.active_pokemon(player_id) is pokemon


async def transformative_start(ctx):
    """Trade yourself out of the Active spot for a Basic from the deck."""
    ditto = ctx.source
    if ditto is None:
        return
    picks = await ctx.search_deck(
        _is_other_basic, count=1, minimum=1,
        prompt="Choose a Basic Pokémon to put in this Pokémon's place.",
    )
    if not picks:
        await ctx.shuffle_deck()
        return
    await ctx.identity_swap(ditto, picks[0], destination="discard",
                            transfer=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="11212320-f347-5006-9ffc-40de3bad48f8",
    key="SV035",
    name=DITTO_NAME,
    display_name="Ditto",
    searchable_by=["Ditto", "Basic", "Ditto"],
    subtypes=["Basic"],
    collector_number=132,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=132,
    abilities=[
        Ability(
            title="Transformative Start",
            game_text="Once during your first turn, if this Pokémon is in the Active Spot, you may search your deck and choose a Basic Pokémon you find there, except any Ditto. Discard this Pokémon and all attached cards, and put that Basic Pokémon in this Pokémon's place. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_transformative_start_condition,
            effect=transformative_start,
        ),
        Attack(
            title="Splup",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
