"""Gothorita (RSV10PT5 42 -- JP SV11W 039; English WHT/125, WHT/42). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def fortunate_eye(ctx):
    await ctx.reorder_deck_top(5, player_id=ctx.opponent_id,
                               prompt="Rearrange the top cards of your opponent's deck")


card = PokemonCardDef(
    guid="2eec8a4c-98b9-5139-9b6a-1c12fcd26a5a",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name",
    display_name="Gothorita",
    searchable_by=["Gothorita", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gothita.Name",
    family_id=574,
    abilities=[
        Attack(
            title="Fortunate Eye",
            game_text="Look at the top 5 cards of your opponent's deck and put them back in any order.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=fortunate_eye,
        ),
        Attack(
            title="Psyshot",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
