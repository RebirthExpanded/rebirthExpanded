"""Pachirisu (SVP 158 -- JP SVP 129; English SVP/158). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_lightning(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.LIGHTNING)


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


async def crackling_charge(ctx):
    heads = sum(1 for r in await ctx.flip_coins(3, "Crackling Charge") if r)
    if heads:
        await _discard_to_bench(ctx, _basic_lightning, heads, f"Attach up to {heads} Basic Lightning Energy cards to your Benched Pokémon")


card = PokemonCardDef(
    guid="2d09a185-4f0c-58ce-a795-d3d2c3a5e7b4",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pachirisu.Name",
    display_name="Pachirisu",
    searchable_by=["Pachirisu", "Basic"],
    subtypes=["Basic"],
    collector_number=158,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=417,
    abilities=[
        Attack(
            title="Crackling Charge",
            game_text="Flip 3 coins. Attach a number of Basic Lightning Energy cards up to the number of heads from your discard pile to your Benched Pokémon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=crackling_charge,
        ),
        Attack(
            title="Tiny Bolt",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
