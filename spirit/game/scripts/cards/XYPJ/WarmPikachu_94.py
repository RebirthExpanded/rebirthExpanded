"""Warm Pikachu (XYPJ 94 -- JP XYP 094; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac



async def _warm_up(ctx):
    await ctx.heal(20, ctx.attacker)
    await ctx.cure_all_conditions(ctx.attacker)


card = PokemonCardDef(
    guid="355bf83d-2918-5d37-8b79-6620ce0830c0",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WarmPikachu.Name",
    display_name="Warm Pikachu",
    searchable_by=["Warm Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Warm Up",
            game_text="Heal 20 damage from this Pokémon and it recovers from all Special Conditions.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_warm_up,
        ),
        Attack(
            title="Thunder Shock",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
