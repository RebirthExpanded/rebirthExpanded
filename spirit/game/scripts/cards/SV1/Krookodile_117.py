"""Krookodile (SV1 117 -- JP SV1S 044; English SVI/117). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def chomp_chomp_bite(ctx):
    await ctx.deal_damage()
    heads = await ctx.flip_until_tails("Chomp Chomp Bite")
    d = ctx.opponent_active()
    if not heads or d is None or d in ctx.knockouts or ctx.effects_blocked(d):
        return
    n = min(heads, len(ctx.attached_energies(d)))
    if n:
        await ctx.discard_energy_from(d, n, minimum=n, prompt=f"Choose {n} Energy to discard")


card = PokemonCardDef(
    guid="43dc7a35-7447-51ed-925d-ad1f2f779dfb",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krookodile.Name",
    display_name="Krookodile",
    searchable_by=["Krookodile", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=117,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    family_id=551,
    abilities=[
        Attack(
            title="Chomp Chomp Bite",
            game_text="Flip a coin until you get tails. For each heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            effect=chomp_chomp_bite,
        ),
        Attack(
            title="Earthquake",
            game_text="This attack also does 30 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2},
            damage=180,
            effect=ac.spread_damage(30, side="mine", also_base=True),
        ),
    ],
)
