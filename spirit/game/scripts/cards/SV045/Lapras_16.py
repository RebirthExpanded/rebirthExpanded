"""Lapras (SV045 16 -- JP SV3a 002; English PAF/16). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card


async def into_the_deep(ctx):
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if pool:
        picks = await ctx.choose_cards(pool, min(3, len(pool)), minimum=0, prompt="Choose up to 3 Basic Energy cards")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="cc187f1c-b25d-555a-8472-a6e79fd1295e",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name",
    display_name="Lapras",
    searchable_by=["Lapras", "Basic"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=131,
    abilities=[
        Attack(
            title="Into the Deep",
            game_text="Put up to 3 Basic Energy cards from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=into_the_deep,
        ),
        Attack(
            title="Freeze-Dry",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
