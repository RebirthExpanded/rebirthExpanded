"""Heat Rotom ex (ME6 15 -- JP M6 015; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fire(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIRE)



async def reheat(ctx):
    pool = [c for c in ctx.discard_pile() if _basic_fire(c)]
    if pool:
        await ctx.reveal_cards(pool)
    await ctx.deal_damage(30 * len(pool))
    if pool:
        await ctx.shuffle_into_deck(pool, ctx.player_id)


card = PokemonCardDef(
    guid="f9d41bae-e29a-52e4-b481-2c9e718d44dc",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HeatRotomex.Name",
    display_name="Heat Rotom ex",
    searchable_by=["Heat Rotom ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=15,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=479,
    abilities=[
        Attack(
            title="Reheat",
            game_text="Reveal all Basic Fire Energy cards from your discard pile. This attack does 30 damage for each card you revealed in this way. Then, shuffle the revealed cards into your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=reheat,
        ),
        Attack(
            title="Strong Flare",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=ac.self_energy_discard_attack(count=2),
        ),
    ],
)
