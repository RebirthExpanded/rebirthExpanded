"""Levincia (SV - Journey Together 150/190 -- JP SV9 098/100).

Stadium.

  "Once during each player's turn, that player may put up to 2 Basic [L]
   Energy cards from their discard pile into their hand."

Mystery Garden's once-per-turn-for-each-player Stadium ability.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.data_utils import Ability, Activations, StadiumCardDef
from spirit.game.session.effects import is_basic_energy


def _basic_lightning(card) -> bool:
    return is_basic_energy(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value)


def levincia_condition(board, player_id, stadium=None):
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(_basic_lightning(c) for c in discard.children)


async def levincia(ctx):
    pool = [c for c in ctx.discard_pile() if _basic_lightning(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=1,
                                   prompt="Choose up to 2 Basic [L] Energy cards to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


card = StadiumCardDef(
    guid="8d24792b-df24-5592-8832-4861c15c1649",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Levincia.Name",
    display_name="Levincia",
    searchable_by=["Levincia", "Stadium", "Levincia"],
    subtypes=["Stadium"],
    collector_number=150,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Levincia",
        game_text="Once during each player's turn, that player may put up to 2 Basic [L] Energy cards from their discard pile into their hand.",
        activation=Activations.ONCE_PER_TURN,
        effect=levincia,
        condition=levincia_condition,
    ),
)
