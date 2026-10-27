"""Castform Sunny Form (SV08 20 -- JP SV7a 006; English SSP/195, SSP/20). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


async def sunny_assist(ctx):
    await ctx.deal_damage()
    pool = list(ctx.attached_energies(ctx.attacker))
    bench = ctx.my_bench()
    if pool and bench and ctx.attacker not in ctx.knockouts:
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to move all Energy to")
        if target is not None:
            for e in pool:
                await ctx.move_energy(e, target)


card = PokemonCardDef(
    guid="e8383338-6e22-5c67-83f9-4f61feddc772",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CastformSunnyForm.Name",
    display_name="Castform Sunny Form",
    searchable_by=["Castform Sunny Form", "Basic"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    family_id=351,
    abilities=[
        Attack(
            title="Singe",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=ac.condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Sunny Assist",
            game_text="Move all Energy from this Pokémon to 1 of your Benched Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=sunny_assist,
        ),
    ],
)
