"""Rapidash (SV10 30 -- JP SV9a 014; English DRI/189, DRI/30). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

def _has_deck(board, player_id, pokemon) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def hurried_gait(ctx):
    await ctx.draw_cards(1)


card = PokemonCardDef(
    guid="1aa6280f-83e7-5530-8ec6-553b9217a5aa",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rapidash.Name",
    display_name="Rapidash",
    searchable_by=["Rapidash", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name",
    family_id=77,
    abilities=[
        Ability(
            title="Hurried Gait",
            game_text="Once during your turn, you may draw a card.",
            activation=Activations.ONCE_PER_TURN,
            condition=_has_deck,
            effect=hurried_gait,
        ),
        Attack(
            title="Fire Mane",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
