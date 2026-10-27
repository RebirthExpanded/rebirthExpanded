"""Kilowattrel (SV08 67 -- JP SV8 043; English SSP/67). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def storm_bolt(ctx):
    await ctx.deal_damage()
    pool = list(ctx.attached_energies(ctx.attacker))
    bench = ctx.my_bench()
    if not pool or not bench or ctx.attacker in ctx.knockouts:
        return
    for e in pool:
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to move the Energy to")
        if target is not None:
            await ctx.move_energy(e, target)


card = PokemonCardDef(
    guid="0c593580-85ab-51c3-bc73-cac77b64fae2",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kilowattrel.Name",
    display_name="Kilowattrel",
    searchable_by=["Kilowattrel", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wattrel.Name",
    family_id=940,
    abilities=[
        Attack(
            title="Glide",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Storm Bolt",
            game_text="Move all Energy from this Pokémon to your Benched Pokémon in any way you like.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=storm_bolt,
        ),
    ],
)
