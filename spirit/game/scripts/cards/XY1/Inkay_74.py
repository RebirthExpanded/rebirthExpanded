"""Inkay (XY 74/146 -- JP XY1-By 035/060, the art here).

Basic Darkness Pokemon. HP 60, weakness Fighting x2, resistance Psychic
-20, retreat 1.

  Upside-Down Evolution  (Ability)  Once during your turn (before your
                                    attack), if this Pokemon is Confused,
                                    you may search your deck for a card
                                    that evolves from this Pokemon and put
                                    it onto this Pokemon. (This counts as
                                    evolving this Pokemon.) Shuffle your
                                    deck afterward.
  Confusion Wave         [D]        Both Active Pokemon are now Confused.

The evolution goes through ctx.evolve_pokemon (Rare Candy's path), which
ignores the may-evolve turn rules -- an Inkay that came down this turn
still evolves -- and the evolution's own on-evolve Abilities fire as on
any evolution. Evolving cures the Confusion, as the rules have it.
"""

from spirit.game.attributes import (
    AttrID, CLIENT_SPECIAL_CONDITION_NAMES, PokemonStage, PokemonTypes, Rarities,
    SpecialConditions,
)
from spirit.game.data_utils import (
    Ability, Activations, Attack, PokemonCardDef, evolves_from,
)
from spirit.game.session.effects import is_pokemon_card

_CONFUSED = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.CONFUSED]


def _confused(board, player_id, pokemon) -> bool:
    return _CONFUSED in (pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


def _evolutions_of(cards, pokemon):
    logic_name = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    return [c for c in cards
            if is_pokemon_card(c) and logic_name and evolves_from(c.archetype_id, logic_name)]


async def upside_down_evolution(ctx):
    inkay = ctx.source
    picks = await ctx.search_deck(
        lambda c: bool(_evolutions_of([c], inkay)), count=1, minimum=0,
        prompt="Choose a card that evolves from Inkay to put onto it.")
    if picks:
        await ctx.evolve_pokemon(inkay, picks[0])
    await ctx.shuffle_deck()


async def confusion_wave(ctx):
    for pokemon in (ctx.opponent_active(), ctx.my_active()):
        if pokemon is not None:
            await ctx.apply_special_condition(pokemon, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="7e3251e8-b5a9-503d-8d55-870e1a75d257",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    display_name="Inkay",
    searchable_by=["Inkay", "Basic"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="XY1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=686,
    abilities=[
        Ability(
            title="Upside-Down Evolution",
            game_text="Once during your turn (before your attack), if this Pokémon is Confused, you may search your deck for a card that evolves from this Pokémon and put it onto this Pokémon. (This counts as evolving this Pokémon.) Shuffle your deck afterward.",
            activation=Activations.ONCE_PER_TURN,
            condition=_confused,
            effect=upside_down_evolution,
        ),
        Attack(
            title="Confusion Wave",
            game_text="Both Active Pokémon are now Confused.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=confusion_wave,
        ),
    ],
)
