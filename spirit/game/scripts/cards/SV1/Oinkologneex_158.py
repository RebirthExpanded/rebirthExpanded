"""Oinkologne ex (SV1 158 -- JP SV1S 068; English SVI/158, SVI/234). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def heavy_stomp(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Heavy Stomp")
    if results and not results[0]:
        ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="e0b1829a-cea9-5dfa-85a4-6e745f3d0532",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oinkologneex.Name",
    display_name="Oinkologne ex",
    searchable_by=["Oinkologne ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=158,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lechonk.Name",
    family_id=915,
    abilities=[
        Attack(
            title="Maddening Scent",
            game_text="This attack does 30 more damage for each of your opponent's Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=ac.damage_per(ac.count_bench("opponent"), 30, base=10),
        ),
        Attack(
            title="Heavy Stomp",
            game_text="Flip a coin. If tails, during your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=210,
            effect=heavy_stomp,
        ),
    ],
)
