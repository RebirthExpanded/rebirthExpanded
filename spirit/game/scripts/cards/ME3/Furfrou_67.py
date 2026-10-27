"""Furfrou (ME3 67 -- JP M3 066; English POR/67). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def hand_trim(ctx):
    excess = len(ctx.hand(ctx.opponent_id)) - 5
    if excess > 0:
        await ac.discard_random_from_hand(ctx, ctx.opponent_id, count=excess)


card = PokemonCardDef(
    guid="1b4dadf4-65cf-5866-9aa3-bb025f941f3c",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Furfrou.Name",
    display_name="Furfrou",
    searchable_by=["Furfrou", "Basic"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=676,
    abilities=[
        Attack(
            title="Hand Trim",
            game_text="Discard random cards from your opponent's hand until they have 5 cards in their hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=hand_trim,
        ),
        Attack(
            title="Headbutt",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
