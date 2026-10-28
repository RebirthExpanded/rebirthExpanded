"""Skwovet (SV1 151 -- JP SV1V 061; English PAF/205, SVI/151, SVI/222). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

def _stash_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand and hand.children)


async def nest_stash(ctx):
    hand = list(ctx.hand())
    if not hand:
        return
    import random
    random.shuffle(hand)
    for card in hand:
        await ctx.put_on_bottom_of_deck(card)
    await ctx.draw_cards(1)


card = PokemonCardDef(
    guid="7845ba62-9006-5d4b-af5a-7bbafa3c9104",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skwovet.Name",
    display_name="Skwovet",
    searchable_by=["Skwovet", "Basic"],
    subtypes=["Basic"],
    collector_number=151,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=819,
    abilities=[
        Ability(
            title="Nest Stash",
            game_text="Once during your turn, you may shuffle your hand and put it on the bottom of your deck. If you put any cards on the bottom of your deck in this way, draw a card.",
            activation=Activations.ONCE_PER_TURN,
            condition=_stash_condition,
            effect=nest_stash,
        ),
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
