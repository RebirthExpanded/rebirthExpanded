"""Volcanion (SV4 22 -- JP SVEL 004; English PAR/22). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fire(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIRE)


async def dual_turbo(ctx):
    await ctx.deal_damage()
    bench = list(ctx.my_bench())
    if not bench:
        return
    chosen = await ctx.choose_cards(bench, min(2, len(bench)), minimum=0, prompt="Choose up to 2 of your Benched Pokémon")
    for p in chosen:
        pool = [c for c in ctx.discard_pile() if _basic_fire(c)]
        if not pool:
            break
        await ctx.attach_energy(pool[0], p)


card = PokemonCardDef(
    guid="93a11899-4dd3-5180-92a5-10b3003060d8",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcanion.Name",
    display_name="Volcanion",
    searchable_by=["Volcanion", "Basic"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=721,
    abilities=[
        Attack(
            title="Dual Turbo",
            game_text="Choose up to 2 of your Benched Pokémon and attach a Basic Fire Energy card from your discard pile to each of them.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=dual_turbo,
        ),
        Attack(
            title="Heavy Impact",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
        ),
    ],
)
