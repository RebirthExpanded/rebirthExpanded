"""Alolan Meowth (SMPJ 255 -- JP SMP 255; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.data_utils import def_for


def _is_hammer(card) -> bool:
    return card is not None and getattr(def_for(card.archetype_id), "display_name", "") == "Wait and See Hammer"


def _box_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(_is_hammer(c) for c in hand.children)


async def dismissal_box(ctx):
    """Discard a Wait and See Hammer from your hand. Then, draw 2 cards."""
    hammers = [c for c in ctx.hand() if _is_hammer(c)]
    if not hammers:
        return
    if await ctx.discard_cards(hammers[:1]) is False:
        return
    await ctx.draw_cards(2)


card = PokemonCardDef(
    guid="55a02eca-131a-550d-9122-0bb92a16c562",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMeowth.Name",
    display_name="Alolan Meowth",
    searchable_by=["Alolan Meowth", "Basic"],
    subtypes=["Basic"],
    collector_number=255,
    set_code="SMPJ",
    regulation_mark="B",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=52,
    abilities=[
        Ability(
            title="Dismissal Box",
            game_text="Once during your turn, you may discard a Wait and See Hammer from your hand. If you do, draw 2 cards.",
            activation=Activations.ONCE_PER_TURN,
            condition=_box_condition,
            effect=dismissal_box,
        ),
        Attack(
            title="Scratch",
            game_text="",
            cost={},
            damage=10,
        ),
    ],
)
