"""Lucky Energy (SWSH - Chilling Reign 158/198).

Special Energy.

  "As long as this card is attached to a Pokemon, it provides [C] Energy."
  "If the Pokemon this card is attached to is in the Active Spot and is
   damaged by an attack from your opponent's Pokemon (even if it is Knocked
   Out), draw a card."

Spiky Energy's granted ON_DAMAGED_BY_ATTACK hook; the holder's owner draws.
"""

from spirit.game.data_utils import EnergyCardDef, Ability, Triggers
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot


async def _lucky_energy_trigger(ctx):
    pokemon = ctx.source
    if not is_in_active_spot(pokemon):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    await ctx.draw_cards(1, player_id=pokemon.owning_player_id)


card = EnergyCardDef(
    guid="e66efd6e-a8c3-5233-aa0a-11c17f1fe25f",
    key="SWSH6",
    name="Lucky Energy",
    display_name="Lucky Energy",
    searchable_by=["Lucky Energy", "Special"],
    subtypes=["Special"],
    collector_number=158,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    granted_abilities=[
        Ability(
            title="Lucky Energy",
            game_text="If the Pokémon this card is attached to is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if it is Knocked Out), draw a card.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=_lucky_energy_trigger,
        ),
    ],
)
