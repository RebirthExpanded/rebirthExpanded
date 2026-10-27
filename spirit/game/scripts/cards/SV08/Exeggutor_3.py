"""Exeggutor (SV08 3 -- JP SV8 002; English SSP/3). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def barrage_oclock(ctx):
    n = len(ctx.attached_energies(ctx.attacker))
    d = ctx.opponent_active()
    if d is not None:
        n += len(ctx.attached_energies(d))
    heads = sum(1 for r in await ctx.flip_coins(n, "Barrage O'Clock") if r) if n else 0
    if heads:
        await ctx.deal_damage(60 * heads)


card = PokemonCardDef(
    guid="71d5753c-8bf5-563b-bf25-a7bac448ce5c",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggutor.Name",
    display_name="Exeggutor",
    searchable_by=["Exeggutor", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=3,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    abilities=[
        Attack(
            title="Barrage O'Clock",
            game_text="Flip a coin for each Energy attached to both Active Pokémon. This attack does 60 damage for each heads.",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            damage_operator="x",
            effect=barrage_oclock,
        ),
    ],
)
