"""Pretend Gyarados Pikachu (XYPJ 151 -- JP XYP 151; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

_discard_all = ac.self_energy_discard_attack(all_energy=True)
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
    guid="edf3dd43-54f1-5c08-94b5-32384a8258cb",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PretendGyaradosPikachu.Name",
    display_name="Pretend Gyarados Pikachu",
    searchable_by=["Pretend Gyarados Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=151,
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
            title="Try Raging",
            game_text="Flip a coin. If heads, this attack does 10 damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=_flip_per_own_counter(10),
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=_discard_all,
        ),
    ],
)
