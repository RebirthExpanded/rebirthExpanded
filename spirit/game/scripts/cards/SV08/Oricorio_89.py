"""Oricorio (SV08 89 -- JP SVLN 007; English SSP/89). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
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
    guid="ee568ee0-d51e-50cf-a3be-a7524ed8d5ae",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name",
    display_name="Oricorio",
    searchable_by=["Oricorio", "Basic"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=741,
    abilities=[
        Attack(
            title="Energy Assist",
            game_text="Attach up to 2 Basic Energy cards from your discard pile to 1 of your Benched Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=energy_assist,
        ),
        Attack(
            title="Dazzle Dance",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
