"""Purrloin (SM - Unified Minds 135/236 -- JP SM11 057/094).

Basic Darkness. HP 70, weakness Fighting x2, resistance Psychic -20,
retreat 1.

  Cleaning Up  [C]  Discard a Pokemon Tool card from 1 of your opponent's
                    Pokemon.

Field Blower's target list narrowed to one side and one card: only their
Tools, exactly one, and no Stadium. It deals no damage, so the discard is
the whole attack -- and with no Tool on their board it simply does nothing,
an attack being declarable whatever the state.

Under this pool's rule that every Pokemon Tool is a Pokemon Tool and never
an Item, is_pokemon_tool reads the printed category, so a Float Stone or a
Technical Machine is as much a target as a Choice Band.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_pokemon_tool


async def cleaning_up(ctx):
    """One Tool off one of their Pokemon."""
    tools = [(pokemon, card)
             for pokemon in ctx.opponent_pokemon_in_play()
             for card in pokemon.children if is_pokemon_tool(card)]
    if not tools:
        return
    picks = await ctx.choose_cards(
        [card for _, card in tools], 1, minimum=1,
        prompt="Choose a Pokémon Tool to discard.")
    if picks:
        await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="4e0c88b4-b92d-5dc9-8337-965d2fdf8783",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    display_name="Purrloin",
    searchable_by=["Purrloin", "Basic", "Purrloin"],
    subtypes=["Basic"],
    collector_number=135,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=509,
    abilities=[
        Attack(
            title="Cleaning Up",
            game_text="Discard a Pokémon Tool card from 1 of your opponent's Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=cleaning_up,
        ),
    ],
)
