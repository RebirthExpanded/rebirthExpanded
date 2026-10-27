"""Snorlax (ME3 63 -- JP M3 062; English POR/63). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.trainers import is_basic_energy_card


async def gormandizer(ctx):
    heads = await ctx.flip_until_tails("Gormandizer")
    if heads > 0:
        picks = await ctx.search_deck(is_basic_energy_card, count=heads, minimum=0,
                                      prompt=f"Choose up to {heads} Basic Energy cards to attach to this Pokémon.")
        for energy in picks:
            await ctx.attach_energy(energy, ctx.attacker)
    await ctx.shuffle_deck()


async def collapse(ctx):
    await ctx.deal_damage()
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="fe160eed-aa39-5965-82ef-608a95a05140",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=446,
    abilities=[
        Attack(
            title="Gormandizer",
            game_text="Flip a coin until you get tails. Search your deck for an amount of Basic Energy up to the number of heads and attach it to this Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gormandizer,
        ),
        Attack(
            title="Collapse",
            game_text="This Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=160,
            effect=collapse,
        ),
    ],
)
