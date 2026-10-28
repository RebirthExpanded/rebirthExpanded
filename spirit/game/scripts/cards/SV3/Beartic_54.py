"""Beartic (SV3 54 -- JP SV3 027; English OBF/54). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def frost_purge(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Frost Purge")
    pool = list(ctx.attached_energies(ctx.attacker))
    if results and not results[0] and pool and ctx.attacker not in ctx.knockouts:
        await ctx.discard_cards(pool)


card = PokemonCardDef(
    guid="67a04f65-7b4b-5997-8134-0882063cc3fe",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beartic.Name",
    display_name="Beartic",
    searchable_by=["Beartic", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubchoo.Name",
    family_id=613,
    abilities=[
        Attack(
            title="Icicle Punch",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
        Attack(
            title="Frost Purge",
            game_text="Flip a coin. If tails, discard all Energy from this Pokémon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=frost_purge,
        ),
    ],
)
