"""Passimian (SV2 118 -- JP SV2D 044; English PAL/118). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _move_one_energy_to_bench(ctx, pred=None):
    pool = [e for e in ctx.attached_energies(ctx.attacker) if pred is None or pred(e)]
    bench = ctx.my_bench()
    if not pool or not bench or ctx.attacker in ctx.knockouts:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Energy to move")
    dest = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to move it to") if picks else None
    if dest is not None:
        await ctx.move_energy(picks[0], dest)


async def make_the_assist(ctx):
    await ctx.deal_damage()
    await _move_one_energy_to_bench(ctx)


card = PokemonCardDef(
    guid="f296f892-5cfd-5156-9471-b865d9e806a0",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Passimian.Name",
    display_name="Passimian",
    searchable_by=["Passimian", "Basic"],
    subtypes=["Basic"],
    collector_number=118,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=766,
    abilities=[
        Attack(
            title="Make the Assist",
            game_text="Move an Energy from this Pokémon to 1 of your Benched Pokémon.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=70,
            effect=make_the_assist,
        ),
    ],
)
