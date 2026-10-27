"""Decidueye (SV065 5 -- JP SV6a 005; English SFA/5). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_grass(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.GRASS)


async def stock_up_on_feathers(ctx):
    await ctx.draw_until(7)


async def power_shot(ctx):
    if not any(_basic_grass(c) for c in ctx.hand()):
        return
    paid = await ctx.discard_from_hand(1, minimum=1, predicate=_basic_grass,
                                       prompt="Discard a Basic Grass Energy card from your hand.")
    if paid:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="fe214864-c1f4-5b88-afb4-26ad12726f83",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Decidueye.Name",
    display_name="Decidueye",
    searchable_by=["Decidueye", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name",
    family_id=722,
    abilities=[
        Attack(
            title="Stock Up on Feathers",
            game_text="Draw cards until you have 7 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=stock_up_on_feathers,
        ),
        Attack(
            title="Power Shot",
            game_text="Discard a Basic Grass Energy card from your hand. If you can't, this attack does nothing.",
            cost={PokemonTypes.GRASS: 1},
            damage=170,
            effect=power_shot,
        ),
    ],
)
