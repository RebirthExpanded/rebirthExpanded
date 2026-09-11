"""Electric Generator (SV - Scarlet & Violet 170/198 -- JP SV1V 069/078).

Item.  "Look at the top 5 cards of your deck and attach up to 2 Basic [L]
Energy cards you find there to your Benched [L] Pokemon in any way you
like. Shuffle the other cards back into your deck."
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import distribute_energy, requires_deck
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_basic_energy, is_pokemon_of_type


def _basic_lightning_energy(card) -> bool:
    return is_basic_energy(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value)


def _benched_lightning(board, player_id):
    return [p for p in board.pokemon_in_play(player_id)
            if not is_in_active_spot(p) and is_pokemon_of_type(p, PokemonTypes.LIGHTNING)]


def _condition(board, player_id, pokemon=None) -> bool:
    return requires_deck(1)(board, player_id) and bool(_benched_lightning(board, player_id))


async def electric_generator(ctx):
    top = ctx.deck_top(5)
    if not top:
        return
    energies = [c for c in top if _basic_lightning_energy(c)]
    picks = await ctx.choose_cards(
        energies, 2, minimum=0,
        prompt="Choose up to 2 Basic [L] Energy cards to attach to your Benched [L] Pokémon.",
        display_cards=top if len(energies) < len(top) else None)
    targets = _benched_lightning(ctx.board, ctx.player_id)
    if picks and targets:
        await distribute_energy(ctx, picks, targets)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="d9f47b10-c0c7-5643-887d-107cbf1ba456",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ElectricGenerator.Name",
    display_name="Electric Generator",
    searchable_by=["Electric Generator", "Item", "ElectricGenerator"],
    subtypes=["Item"],
    collector_number=170,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    regulation_mark="G",
    condition=_condition,
    effect=electric_generator,
)
