"""Golisopod ex (SV4 50 -- JP SV4K 022; English PAR/221, PAR/246, PAR/50). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def swing_and_skedaddle(ctx):
    await ctx.deal_damage()
    pool = list(ctx.attached_energies(ctx.attacker))
    if not pool or ctx.attacker in ctx.knockouts:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Energy to discard from this Pokémon")
    await ctx.discard_cards(picks)
    bench = ctx.my_bench()
    if picks and bench:
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to switch with")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)


card = PokemonCardDef(
    guid="0b86feff-8b05-5005-ada0-6f7f09af72c5",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golisopodex.Name",
    display_name="Golisopod ex",
    searchable_by=["Golisopod ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=50,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    family_id=767,
    abilities=[
        Attack(
            title="Aqua Blade",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
        Attack(
            title="Swing and Skedaddle",
            game_text="Discard an Energy from this Pokémon. If you do, switch it with 1 of your Benched Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=170,
            effect=swing_and_skedaddle,
        ),
    ],
)
