"""Deoxys (SV4 74 -- JP SVEM 006; English PAR/74). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _spread_energy_to_bench(ctx):
    pool = list(ctx.attached_energies(ctx.attacker))
    bench = ctx.my_bench()
    if not pool or not bench or ctx.attacker in ctx.knockouts:
        return
    for e in pool:
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to move the Energy to")
        if target is not None:
            await ctx.move_energy(e, target)


async def genome_spiral(ctx):
    await ctx.deal_damage()
    await _spread_energy_to_bench(ctx)


card = PokemonCardDef(
    guid="c5fa6a54-253a-5e74-b6eb-eb1eef657874",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys",
    searchable_by=["Deoxys", "Basic"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=386,
    abilities=[
        Attack(
            title="Psypunch",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
        Attack(
            title="Genome Spiral",
            game_text="Move all Energy from this Pokémon to your Benched Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=120,
            effect=genome_spiral,
        ),
    ],
)
