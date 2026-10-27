"""Oricorio (SV08 26 -- JP SVLS 004; English SSP/26). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card


async def energy_assist(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not bench or not pool:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Pokémon")
    if target is None:
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Attach up to 2 Basic Energy cards to it")
    for card in picks:
        await ctx.attach_energy(card, target)


card = PokemonCardDef(
    guid="ecb31539-0488-55dc-9e5b-05106b4ca2ae",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name",
    display_name="Oricorio",
    searchable_by=["Oricorio", "Basic"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=741,
    abilities=[
        Attack(
            title="Energy Assist",
            game_text="Attach up to 2 Basic Energy cards from your discard pile to 1 of your Benched Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            effect=energy_assist,
        ),
        Attack(
            title="Fireworks",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
