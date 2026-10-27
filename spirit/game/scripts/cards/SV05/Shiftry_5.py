"""Shiftry (SV05 5 -- JP SV5M 005; English TEF/163, TEF/5). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import full_stack


async def expelling_tornado(ctx):
    bench = list(ctx.opponent_bench())
    if len(bench) <= 3:
        return
    keep = await ctx.choose_cards(bench, 3, minimum=3, prompt="Choose 3 of your opponent's Benched Pokémon to keep")
    for p in bench:
        if p not in keep:
            await ctx.shuffle_into_deck(full_stack(p), ctx.opponent_id)


async def energy_loop(ctx):
    await ctx.deal_damage()
    pool = ctx.attached_energies(ctx.attacker)
    if pool:
        picks = await ctx.choose_cards(list(pool), 1, minimum=1, prompt="Choose an Energy to put into your hand")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="6e829e7c-e43e-5745-b1c3-6c327d219320",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Attack(
            title="Expelling Tornado",
            game_text="Choose 3 of your opponent's Benched Pokémon. If you do, shuffle all of your opponent's Benched Pokémon that you didn't choose, and all cards attached to those Pokémon, into their deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=expelling_tornado,
        ),
        Attack(
            title="Energy Loop",
            game_text="Put an Energy attached to this Pokémon into your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=energy_loop,
        ),
    ],
)
