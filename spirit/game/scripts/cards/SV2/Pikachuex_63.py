"""Pikachu ex (SV2 63 -- JP SVC 001; English PAL/63). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def dynamic_bolt(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Dynamic Bolt")
    pool = list(ctx.attached_energies(ctx.attacker))
    if results and not results[0] and pool and ctx.attacker not in ctx.knockouts:
        await ctx.discard_cards(pool)


card = PokemonCardDef(
    guid="c431fd15-ae00-5cb0-8c1f-66df89512339",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachuex.Name",
    display_name="Pikachu ex",
    searchable_by=["Pikachu ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=63,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Pika Punch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Dynamic Bolt",
            game_text="Flip a coin. If tails, discard all Energy from this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=dynamic_bolt,
        ),
    ],
)
