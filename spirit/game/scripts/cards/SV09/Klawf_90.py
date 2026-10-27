"""Klawf (SV09 90 -- JP SV9 055; English JTG/90). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _discard_opp_energy_for_heads(ctx, coins):
    heads = sum(1 for r in await ctx.flip_coins(coins, ctx.ability.title if ctx.ability else "") if r)
    target = ctx.opponent_active()
    if heads and target is not None and not ctx.effects_blocked(target) and ctx.attached_energies(target):
        n = min(heads, len(ctx.attached_energies(target)))
        await ctx.discard_energy_from(target, n, minimum=n,
                                      prompt=f"Choose {n} Energy to discard from your opponent's Active Pokémon")


async def snipping_pincers(ctx):
    await _discard_opp_energy_for_heads(ctx, 2)


card = PokemonCardDef(
    guid="8b2bf121-d917-5755-83c6-20b671d1004c",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klawf.Name",
    display_name="Klawf",
    searchable_by=["Klawf", "Basic"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=950,
    abilities=[
        Attack(
            title="Snipping Pincers",
            game_text="Flip 2 coins. For each heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=snipping_pincers,
        ),
        Attack(
            title="Hammer In",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
