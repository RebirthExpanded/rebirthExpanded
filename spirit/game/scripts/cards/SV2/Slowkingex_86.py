"""Slowking ex (SV2 86 -- JP SV2P 030; English PAL/238, PAL/86). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


async def wise_headbutt(ctx):
    await ctx.deal_damage()
    if not ctx.deck_top(1) or not await ctx.ask_yes_no("Search your deck for up to 2 cards?"):
        return
    picks = await ctx.search_deck(count=2, minimum=0, prompt="Choose up to 2 cards to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="152a9590-c452-5984-b4a5-4123e7ba14a2",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowkingex.Name",
    display_name="Slowking ex",
    searchable_by=["Slowking ex", "Stage 1", "ex", "Tera"],
    subtypes=["Stage 1", "ex", "Tera"],
    collector_number=86,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Profound Knowledge",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Wise Headbutt",
            game_text="You may search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=130,
            effect=wise_headbutt,
        ),
    ],
)
