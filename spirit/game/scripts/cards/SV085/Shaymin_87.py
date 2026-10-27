"""Shaymin (SV085 87 -- JP SVM 105; English PRE/87). Japanese art.
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


async def reflect_energy(ctx):
    await ctx.deal_damage()
    await _move_one_energy_to_bench(ctx)


card = PokemonCardDef(
    guid="bf85eb51-b108-5ff7-a18a-7bb7d314a42d",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name",
    display_name="Shaymin",
    searchable_by=["Shaymin", "Basic"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=492,
    abilities=[
        Attack(
            title="Reflect Energy",
            game_text="Move an Energy from this Pokémon to 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=reflect_energy,
        ),
    ],
)
