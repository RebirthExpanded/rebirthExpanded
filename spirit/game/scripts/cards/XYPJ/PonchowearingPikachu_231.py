"""Poncho-wearing Pikachu (XYPJ 231 -- JP XYP 231; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac



def _flip_per_own_counter(per):
    """Flip a coin. If heads, this attack does `per` damage for each damage
    counter on this Pokemon (tails: nothing)."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "")
        if not (results and results[0]):
            return
        counters = ac.damage_counters_on("self")(ctx)
        if counters:
            await ctx.deal_damage(per * counters)
    return effect


card = PokemonCardDef(
    guid="799e2fca-8262-5a81-9b47-c7ef29e0cffb",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PonchowearingPikachu.Name",
    display_name="Poncho-wearing Pikachu",
    searchable_by=["Poncho-wearing Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=231,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Pika Punch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Outrage?",
            game_text="Flip a coin. If heads, this attack does 20 damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=_flip_per_own_counter(20),
        ),
    ],
)
