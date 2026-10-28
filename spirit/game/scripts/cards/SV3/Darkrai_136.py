"""Darkrai (SV3 136 -- JP SV3 074; English OBF/136). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


async def night_cyclone(ctx):
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
    guid="4870af63-ec72-5342-85f9-a21747b2292d",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darkrai.Name",
    display_name="Darkrai",
    searchable_by=["Darkrai", "Basic"],
    subtypes=["Basic"],
    collector_number=136,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=491,
    abilities=[
        Attack(
            title="Dark Slumber",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Night Cyclone",
            game_text="Move all Energy from this Pokémon to your Benched Pokémon in any way you like.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=night_cyclone,
        ),
    ],
)
