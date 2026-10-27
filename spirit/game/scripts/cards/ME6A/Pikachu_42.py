"""Pikachu (ME6A 42 -- JP M6a 042; English 30C/48). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card


async def store_up(ctx):
    pool = [c for c in ctx.recoverable_discard() if is_basic_energy_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0,
                                   prompt="Choose up to 2 Basic Energy cards to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="911e48d1-50db-57cc-8cb9-d4e3bd4b123d",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Store Up",
            game_text="Put up to 2 Basic Energy cards from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=store_up,
        ),
    ],
)
