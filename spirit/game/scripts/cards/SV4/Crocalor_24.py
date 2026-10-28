"""Crocalor (SV4 24 -- JP SVEL 006; English PAR/24). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def rolling_fireball(ctx):
    await ctx.deal_damage()
    pool = list(ctx.attached_energies(ctx.attacker))
    if pool and ctx.attacker not in ctx.knockouts:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Energy to put into your hand")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="c86e3035-ecd7-5a63-bc04-0f51e285a69b",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crocalor.Name",
    display_name="Crocalor",
    searchable_by=["Crocalor", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fuecoco.Name",
    family_id=909,
    abilities=[
        Attack(
            title="Rolling Fireball",
            game_text="Put an Energy attached to this Pokémon into your hand.",
            cost={PokemonTypes.FIRE: 2},
            damage=90,
            effect=rolling_fireball,
        ),
    ],
)
