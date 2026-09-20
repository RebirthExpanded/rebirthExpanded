"""Skiploom (SM - Lost Thunder 14/214 -- JP SM8 010/095, the art here).

Stage 1 Grass Pokemon (evolves from Hoppip). HP 60, weakness Lightning
x2, resistance Fighting -20, retreat 0.

  Floral Path to the Sky  (Ability)  Once during your turn (before your
                                     attack), you may search your deck for
                                     Jumpluff. Then, put this Pokemon and
                                     all cards attached to it in the Lost
                                     Zone and put that Jumpluff in its
                                     place. Shuffle your deck afterward.
  Tackle                  [G] 30

Palafin's Zero to Hero shape: the Jumpluff from the deck takes Skiploom's
exact spot (identity_swap, transfer=False), Skiploom and everything
attached go to the Lost Zone, and the deck is shuffled either way.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, def_for


def _is_jumpluff(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", "") == "Jumpluff"


def _deck_not_empty(board, player_id, pokemon=None) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def floral_path_to_the_sky(ctx):
    picks = await ctx.search_deck(
        _is_jumpluff, count=1, minimum=0,
        prompt="Choose a Jumpluff to put in this Pokémon's place.")
    if picks:
        await ctx.identity_swap(ctx.source, picks[0], destination="lostZone", transfer=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="7aa73499-6ba0-51d9-906b-a5183dd5de63",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name",
    display_name="Skiploom",
    searchable_by=["Skiploom", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name",
    family_id=187,
    abilities=[
        Ability(
            title="Floral Path to the Sky",
            game_text="Once during your turn (before your attack), you may search your deck for Jumpluff. Then, put this Pokémon and all cards attached to it in the Lost Zone and put that Jumpluff in its place. Shuffle your deck afterward.",
            activation=Activations.ONCE_PER_TURN,
            condition=_deck_not_empty,
            effect=floral_path_to_the_sky,
        ),
        Attack(title="Tackle", game_text="", cost={PokemonTypes.GRASS: 1}, damage=30),
    ],
)
