"""Mesprit (SV08 79 -- JP SV8 049; English SSP/204, SSP/79). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_psychic(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.PSYCHIC)
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


async def full_heart(ctx):
    pool = [c for c in ctx.hand() if _basic_psychic(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Attach up to 2 Basic Psychic Energy cards")
    for card in picks:
        target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon to attach it to")
        if target is not None:
            await ctx.attach_energy(card, target)


async def guardian_burst(ctx):
    names = {p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) for p in ctx.my_bench()}
    if "Uxie" in names and "Azelf" in names:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="b5b730d7-fe62-5fe9-a892-c814a23b09b8",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mesprit.Name",
    display_name="Mesprit",
    searchable_by=["Mesprit", "Basic"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=481,
    abilities=[
        Attack(
            title="Full Heart",
            game_text="Attach up to 2 Basic Psychic Energy cards from your hand to your Pokémon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=full_heart,
        ),
        Attack(
            title="Guardian Burst",
            game_text="If you don't have Uxie and Azelf on your Bench, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=160,
            effect=guardian_burst,
        ),
    ],
)
