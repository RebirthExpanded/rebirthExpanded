"""Chien-Pao ex (SV - Paldea Evolved 61/193 -- JP SV2P 028/071).

Basic Water Pokemon ex. HP 220, weakness Metal x2, retreat 2.

  Ability  Shivery Chill  Once during your turn, if this Pokemon is in the
                          Active Spot, you may search your deck for up to 2
                          Basic [W] Energy cards, reveal them, and put them
                          into your hand. Then, shuffle your deck.
  Hail Blade  [WW] 60x  You may discard any amount of [W] Energy from your
                        Pokemon. This attack does 60 damage for each card
                        you discarded in this way.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import requires_deck
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)
from spirit.game.session.effects import is_basic_energy


def _basic_water_energy(card) -> bool:
    return is_basic_energy(card) and energy_provides_type(card, PokemonTypes.WATER.value)


def _shivery_chill_condition(board, player_id, pokemon) -> bool:
    return is_in_active_spot(pokemon) and requires_deck(1)(board, player_id)


async def shivery_chill(ctx):
    picks = await ctx.search_deck(_basic_water_energy, count=2, minimum=0,
                                  prompt="Choose up to 2 Basic [W] Energy cards to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def hail_blade(ctx):
    pool = [e for p in ctx.my_pokemon_in_play() for e in ctx.board.attached_energies(p)
            if energy_provides_type(e, PokemonTypes.WATER.value)]
    picks = await ctx.choose_cards(pool, len(pool), minimum=0,
                                   prompt="Choose any amount of [W] Energy to discard.") if pool else []
    if picks:
        await ctx.discard_cards(picks)
    await ctx.deal_damage(60 * len(picks))


card = PokemonCardDef(
    guid="13a6bc0f-593d-5cad-8f48-b1fc2a63b18a",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChienPaoex.Name",
    display_name="Chien-Pao ex",
    searchable_by=["Chien-Pao ex", "Basic", "ex", "ChienPaoex"],
    subtypes=["Basic", "ex"],
    collector_number=61,
    set_code="SV2",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=1002,
    regulation_mark="G",
    abilities=[
        Ability(title="Shivery Chill",
                game_text="Once during your turn, if this Pokémon is in the Active Spot, you may search your deck for up to 2 Basic [W] Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
                activation=Activations.ONCE_PER_TURN, condition=_shivery_chill_condition,
                effect=shivery_chill),
        Attack(title="Hail Blade",
               game_text="You may discard any amount of [W] Energy from your Pokémon. This attack does 60 damage for each card you discarded in this way.",
               cost={PokemonTypes.WATER: 2}, damage=60, effect=hail_blade),
    ],
)
