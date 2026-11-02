"""Yokohama's Pikachu (SMPJ 281 -- JP SMP 281; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su



async def _sightseeing(ctx):
    """Printed damage. Flip a coin. If heads, switch this Pokemon with 1 of your Benched Pokemon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "")
    if results and results[0]:
        await su.switch_self_attack()(ctx)


card = PokemonCardDef(
    guid="efcb84b2-d97b-531f-8ed0-b26b6548a2f9",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.YokohamasPikachu.Name",
    display_name="Yokohama's Pikachu",
    searchable_by=["Yokohama's Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=281,
    set_code="SMPJ",
    regulation_mark="B",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Sightseeing",
            game_text="Flip a coin. If heads, switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=_sightseeing,
        ),
        Attack(
            title="Thunder Jolt",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.recoil_attack(10),
        ),
    ],
)
