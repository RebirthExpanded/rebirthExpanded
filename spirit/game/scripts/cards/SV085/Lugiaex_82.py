"""Lugia ex (SV085 82 -- JP SVM 097; English PRE/82). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def hyper_whirlpool(ctx):
    await ctx.deal_damage()
    heads = await ctx.flip_until_tails("Hyper Whirlpool")
    d = ctx.opponent_active()
    if not heads or d is None or d in ctx.knockouts or ctx.effects_blocked(d):
        return
    n = min(heads, len(ctx.attached_energies(d)))
    if n:
        await ctx.discard_energy_from(d, n, minimum=n, prompt=f"Choose {n} Energy to discard")


card = PokemonCardDef(
    guid="e6a4158d-02cd-54d6-a786-94843f7d7e7c",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lugiaex.Name",
    display_name="Lugia ex",
    searchable_by=["Lugia ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=82,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=249,
    abilities=[
        Attack(
            title="Hyper Whirlpool",
            game_text="Flip a coin until you get tails. For each heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=140,
            effect=hyper_whirlpool,
        ),
    ],
)
