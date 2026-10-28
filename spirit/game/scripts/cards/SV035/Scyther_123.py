"""Scyther (SV035 123 -- JP SV2a 123; English MEW/123). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_grass(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.GRASS)


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


async def helpful_slash(ctx):
    await ctx.deal_damage()
    await _discard_to_bench(ctx, _basic_grass, 1, "Attach a Basic Grass Energy card to 1 of your Benched Pokémon")


card = PokemonCardDef(
    guid="ef0da448-1a57-53e5-9e15-9ec227c46050",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    display_name="Scyther",
    searchable_by=["Scyther", "Basic"],
    subtypes=["Basic"],
    collector_number=123,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    family_id=123,
    abilities=[
        Attack(
            title="Helpful Slash",
            game_text="Attach a Basic Grass Energy card from your discard pile to 1 of your Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=helpful_slash,
        ),
        Attack(
            title="Slicing Blade",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
