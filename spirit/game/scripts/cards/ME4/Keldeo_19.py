"""Keldeo (ME4 19 -- JP M4 019; English CRI/19). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def reflect_energy(ctx):
    await ctx.deal_damage()
    pool = ctx.attached_energies(ctx.attacker)
    bench = ctx.my_bench()
    if not pool or not bench:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Energy to move to 1 of your Benched Pokémon")
    if picks:
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon")
        if target is not None:
            await ctx.move_energy(picks[0], target)


card = PokemonCardDef(
    guid="5987201d-62f7-5bc3-9d43-159fa6f613d5",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Keldeo.Name",
    display_name="Keldeo",
    searchable_by=["Keldeo", "Basic"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=647,
    abilities=[
        Attack(
            title="Shoot Through",
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=ac.snipe_attack(20, pool="bench", also_base=True),
        ),
        Attack(
            title="Reflect Energy",
            game_text="Move an Energy from this Pokémon to 1 of your Benched Pokémon.",
            cost={PokemonTypes.WATER: 2},
            damage=70,
            effect=reflect_energy,
        ),
    ],
)
