"""Bombirdier ex (SV4 156 -- JP SV3a 051; English PAR/156, PAR/234). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import full_stack


async def _back_to_hand(ctx):
    await ctx.deal_damage()
    me = ctx.attacker
    if me in ctx.knockouts:
        return
    if ctx.board.active_pokemon(ctx.player_id) is me and not ctx.my_bench():
        return
    await ctx.put_in_hand(full_stack(me), reveal=False)


async def shadowy_wind(ctx):
    await ctx.deal_damage()
    me = ctx.attacker
    if me in ctx.knockouts or not ctx.my_bench():
        return
    if await ctx.ask_yes_no("Put this Pokémon and all attached cards into your hand?"):
        from spirit.game.session.effects import full_stack
        await ctx.put_in_hand(full_stack(me), reveal=False)


card = PokemonCardDef(
    guid="fddddec7-4ba0-5944-ba1c-422a85e8ba76",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bombirdierex.Name",
    display_name="Bombirdier ex",
    searchable_by=["Bombirdier ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=156,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=962,
    abilities=[
        Attack(
            title="Fast Carrier",
            game_text="If you go first, you can use this attack during your first turn. Search your deck for up to 3 Basic Pokémon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_bench(count=3, prompt="Choose up to 3 Basic Pokémon to put onto your Bench."),
            usable_first_turn=True,
        ),
        Attack(
            title="Shadowy Wind",
            game_text="You may put this Pokémon and all attached cards into your hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=shadowy_wind,
        ),
    ],
)
