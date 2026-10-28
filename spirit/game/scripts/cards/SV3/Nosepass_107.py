"""Nosepass (SV3 107 -- JP SV3 057; English OBF/107). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_metal(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.METAL)


async def iron_collecting(ctx):
    pool = [c for c in ctx.discard_pile() if _basic_metal(c)]
    if pool:
        picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Choose up to 2 Basic Metal Energy cards")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="5c34fade-6679-568a-8318-fa54edbcf1e6",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name",
    display_name="Nosepass",
    searchable_by=["Nosepass", "Basic"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=299,
    abilities=[
        Attack(
            title="Iron Collecting",
            game_text="Put up to 2 Basic Metal Energy cards from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=iron_collecting,
        ),
        Attack(
            title="Rolling Tackle",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
