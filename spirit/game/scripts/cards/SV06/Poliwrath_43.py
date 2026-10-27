"""Poliwrath (SV06 43 -- JP SV6 025; English TWM/43). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import full_stack


async def jumping_uppercut(ctx):
    if await ctx.ask_yes_no("Do 120 more damage? (This Pokémon and all attached cards are shuffled into your deck.)"):
        await ctx.deal_damage(240)
        if ctx.attacker not in ctx.knockouts:
            await ctx.shuffle_into_deck(full_stack(ctx.attacker), ctx.player_id)
    else:
        await ctx.deal_damage(120)


card = PokemonCardDef(
    guid="4215d0a9-31c2-56e4-bb8b-22fe1d87b150",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwrath.Name",
    display_name="Poliwrath",
    searchable_by=["Poliwrath", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=43,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    family_id=60,
    abilities=[
        Attack(
            title="Hypnosis",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Jumping Uppercut",
            game_text="You may do 120 more damage. If you do, shuffle this Pokémon and all attached cards into your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="+",
            effect=jumping_uppercut,
        ),
    ],
)
