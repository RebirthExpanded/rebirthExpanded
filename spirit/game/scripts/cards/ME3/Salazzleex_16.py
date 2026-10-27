"""Salazzle ex (ME3 16 -- JP M3 016; English POR/101, POR/16). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import support_common as su


async def dire_nails(ctx):
    await ctx.deal_damage()
    target = ctx.opponent_active()
    if target is not None:
        await ctx.apply_special_condition(target, SpecialConditions.BURNED)
        await ctx.apply_special_condition(target, SpecialConditions.POISONED)
    await su.switch_self_attack(damage=0)(ctx)


card = PokemonCardDef(
    guid="6d23cba0-17e1-56ee-b468-f77e80f0d356",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salazzleex.Name",
    display_name="Salazzle ex",
    searchable_by=["Salazzle ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=16,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name",
    family_id=757,
    abilities=[
        Attack(
            title="Nasty Plot",
            game_text="Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=su.search_to_hand(None, count=2, reveal=False, prompt="Choose up to 2 cards."),
        ),
        Attack(
            title="Dire Nails",
            game_text="Your opponent's Active Pokémon is now Burned and Poisoned. Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.FIRE: 2},
            damage=100,
            effect=dire_nails,
        ),
    ],
)
