"""Zacian (SV4 136 -- JP SV3a 048; English PAR/136). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_metal(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.METAL)


async def _discard_to_bench(ctx, pred, upto, prompt):
    bench = ctx.my_bench()
    pool = [c for c in ctx.discard_pile() if pred(c)]
    if not bench or not pool:
        return
    picks = await ctx.choose_cards(pool, min(upto, len(pool)), minimum=0, prompt=prompt)
    for card in picks:
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to attach the Energy to")
        if target is not None:
            await ctx.attach_energy(card, target)


async def iron_roar(ctx):
    await ctx.deal_damage()
    await _discard_to_bench(ctx, _basic_metal, 1, "Attach a Basic Metal Energy card to 1 of your Benched Pokémon")


card = PokemonCardDef(
    guid="5e986d69-2995-5713-b60a-a3b405c98308",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zacian.Name",
    display_name="Zacian",
    searchable_by=["Zacian", "Basic"],
    subtypes=["Basic"],
    collector_number=136,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=888,
    abilities=[
        Attack(
            title="Iron Roar",
            game_text="Attach a Basic Metal Energy card from your discard pile to 1 of your Benched Pokémon.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            effect=iron_roar,
        ),
        Attack(
            title="Brave Blade",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=_hit_then_lock,
        ),
    ],
)
