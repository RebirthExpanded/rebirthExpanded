"""Strange Timepiece (ME - Mega Evolution 128/132 -- JP M1S 057/064, the art here).

Item.

  "Devolve 1 of your evolved [P] Pokemon by putting any number of
   Evolution cards on it into your hand. (That Pokemon can't evolve this
   turn.)"

Devolution Spray with a type filter and a chosen depth: a Stage 2 offers
one step (back to Stage 1) or two (back to the Basic).
"""

from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import devolvable
from spirit.game.data_utils import ItemCardDef
from spirit.game.models.board import PokemonEntity
from spirit.game.session.effects import is_pokemon_of_type


def _evolution_depth(pokemon) -> int:
    """How many Evolution cards sit on the stack (Stage 2 on Stage 1 on
    Basic = 2): the tucked Pokemon cards under the top card, however the
    stack is nested."""
    count = 0
    todo = list(pokemon.children)
    while todo:
        child = todo.pop()
        if isinstance(child, PokemonEntity):
            count += 1
            todo.extend(child.children)
    return count


def _condition(board, player_id, card=None) -> bool:
    return any(devolvable(p) and is_pokemon_of_type(p, PokemonTypes.PSYCHIC)
               for p in board.pokemon_in_play(player_id))


async def strange_timepiece(ctx):
    candidates = [p for p in ctx.my_pokemon_in_play()
                  if devolvable(p) and is_pokemon_of_type(p, PokemonTypes.PSYCHIC)]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your evolved [P] Pokémon to devolve.")
    if target is None:
        return
    depth = _evolution_depth(target)
    steps = 1
    if depth > 1:
        steps = 1 + await ctx.choose(
            "How many Evolution cards will you put into your hand?",
            [str(n) for n in range(1, depth + 1)])
    await ctx.devolve_pokemon(target, steps=steps, destination="hand")


card = ItemCardDef(
    guid="75177866-8d4b-5bbf-99c9-be585b2fa045",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StrangeTimepiece.Name",
    display_name="Strange Timepiece",
    searchable_by=["Strange Timepiece", "Item", "StrangeTimepiece"],
    subtypes=["Item"],
    collector_number=128,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    condition=_condition,
    effect=strange_timepiece,
)
