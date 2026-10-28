"""Tropius (SV2 7 -- JP SV1a 001; English PAL/195, PAL/7). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


async def tropic_breeze(ctx):
    await ctx.deal_damage()
    pool = list(ctx.attached_energies(ctx.attacker))
    bench = ctx.my_bench()
    if pool and bench and ctx.attacker not in ctx.knockouts:
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to move all Energy to")
        if target is not None:
            for e in pool:
                await ctx.move_energy(e, target)


card = PokemonCardDef(
    guid="46a1300c-ef90-5a98-96a7-13fe5af0224e",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tropius.Name",
    display_name="Tropius",
    searchable_by=["Tropius", "Basic"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=357,
    abilities=[
        Attack(
            title="Leaf Drain",
            game_text="Heal 20 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=su.heal_attack(20),
        ),
        Attack(
            title="Tropic Breeze",
            game_text="Move all Energy from this Pokémon to 1 of your Benched Pokémon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=tropic_breeze,
        ),
    ],
)
