"""Herbal Energy (XY - Furious Fists 103/111 -- JP XY3 095/096).

Special Energy.

  "This card can only be attached to [G] Pokemon. This card provides [G]
   Energy only while this card is attached to a [G] Pokemon. When you
   attach this card from your hand to 1 of your [G] Pokemon, heal 30 damage
   from that Pokemon. (If this card is attached to anything other than a
   [G] Pokemon, discard this card.)"

Strong Energy (XY3)'s type-locked shape: attach_to + discard_if_invalid.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import Ability, EnergyCardDef, Triggers, def_for
from spirit.game.session.effects import special_energy_neutralized
from spirit.game.session.effects import is_pokemon_of_type


def _grass_pokemon(pokemon) -> bool:
    return is_pokemon_of_type(pokemon, PokemonTypes.GRASS)


NAME = "Herbal Energy"


def _this_card_from_hand(ctx) -> bool:
    """This Herbal Energy, just attached from my hand (and not switched off)."""
    energy = ctx.attached_energy
    if energy is None or getattr(def_for(energy.archetype_id), "display_name", None) != NAME:
        return False
    return ctx.attaching_player_id == ctx.player_id and not special_energy_neutralized(energy)


def _still_on_that_pokemon(ctx) -> bool:
    """...to this Pokemon, which is still the one in play holding it."""
    pokemon = ctx.source
    return (ctx.energy_receiver is pokemon and ctx.attached_energy.parent is pokemon
            and pokemon in ctx.board.pokemon_in_play(ctx.player_id))


def _herbal_applies(ctx) -> bool:
    return (_this_card_from_hand(ctx) and _still_on_that_pokemon(ctx)
            and _grass_pokemon(ctx.source))


async def herbal_energy(ctx):
    """Attached from hand to a [G] Pokemon: heal 30 from it."""
    if _herbal_applies(ctx):
        await ctx.heal(30, ctx.source)


card = EnergyCardDef(
    guid="22b566a5-3973-53ad-8e4f-30f5c554f6e3",
    key="XY3",
    name="Herbal Energy",
    display_name="Herbal Energy",
    searchable_by=["Herbal Energy", "Special", "HerbalEnergy"],
    subtypes=["Special"],
    collector_number=103,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.GRASS,
    is_special=True,
    attach_to=_grass_pokemon,
    discard_if_invalid=True,
    provides=[[PokemonTypes.GRASS]],
    granted_abilities=[
        Ability(
            title="Herbal Energy",
            game_text="When you attach this card from your hand to 1 of your Grass Pok\u00e9mon, heal 30 damage from that Pok\u00e9mon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=herbal_energy,
            trigger_applies=_herbal_applies,
        ),
    ],
)
