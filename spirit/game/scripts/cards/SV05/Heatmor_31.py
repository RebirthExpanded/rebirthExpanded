"""Heatmor (SV05 31 -- JP SV5K 009; English TEF/31). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def licking_flames(ctx):
    await ctx.deal_damage()
    tails = sum(1 for r in await ctx.flip_coins(3, "Licking Flames") if not r)
    pool = list(ctx.attached_energies(ctx.attacker))
    n = min(tails, len(pool))
    if n and ctx.attacker not in ctx.knockouts:
        picks = await ctx.choose_cards(pool, n, minimum=n, prompt=f"Choose {n} Energy to discard from this Pokémon")
        await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="9dfa67a4-77e3-5d04-9f10-1e4460cdd58e",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatmor.Name",
    display_name="Heatmor",
    searchable_by=["Heatmor", "Basic"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=631,
    abilities=[
        Attack(
            title="Live Coal",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title="Licking Flames",
            game_text="Flip 3 coins. For each tails, discard an Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=licking_flames,
        ),
    ],
)
