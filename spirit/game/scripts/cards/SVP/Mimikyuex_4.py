"""Mimikyu ex (SVP 4 -- JP SVAW 006; English SVP/4). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def strafe(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if bench and ctx.attacker not in ctx.knockouts and await ctx.ask_yes_no("Switch this Pokémon with 1 of your Benched Pokémon?"):
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to switch with")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)


def _both_energy(ctx) -> int:
    return ac.count_energy("self", cards=True)(ctx) + ac.count_energy("defender", cards=True)(ctx)


card = PokemonCardDef(
    guid="7c952077-8288-5cf7-ad0e-850c10f2d610",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyuex.Name",
    display_name="Mimikyu ex",
    searchable_by=["Mimikyu ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=4,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=778,
    abilities=[
        Attack(
            title="Void Return",
            game_text="You may switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=strafe,
        ),
        Attack(
            title="Energy Burst",
            game_text="This attack does 30 damage for each Energy attached to both Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=ac.damage_per(_both_energy, 30),
        ),
    ],
)
