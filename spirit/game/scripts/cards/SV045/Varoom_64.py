"""Varoom (SV045 64 -- JP SV4a 130; English PAF/192, PAF/64). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card


async def rev(ctx):
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if pool:
        picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Choose up to 2 Basic Energy cards")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="f9a255f4-67c9-5252-a7b9-c29cdf87c8d8",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name",
    display_name="Varoom",
    searchable_by=["Varoom", "Basic"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=965,
    abilities=[
        Attack(
            title="Rev",
            game_text="Put up to 2 Basic Energy cards from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=rev,
        ),
        Attack(
            title="Headbutt",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
