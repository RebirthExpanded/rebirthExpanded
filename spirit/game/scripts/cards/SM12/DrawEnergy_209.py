"""Draw Energy (SM - Cosmic Eclipse 209/236 -- JP SM11a 060/064).

Special Energy.

  "This card provides [C] Energy.
   When you attach this card from your hand to a Pokemon, draw a card."
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import Ability, EnergyCardDef, Triggers, def_for
from spirit.game.session.effects import special_energy_neutralized


NAME = "Draw Energy"


def _this_card_from_hand(ctx) -> bool:
    """This Draw Energy, just attached from my hand (and not switched off)."""
    energy = ctx.attached_energy
    if energy is None or getattr(def_for(energy.archetype_id), "display_name", None) != NAME:
        return False
    return ctx.attaching_player_id == ctx.player_id and not special_energy_neutralized(energy)


def _still_on_that_pokemon(ctx) -> bool:
    """...to this Pokemon, which is still the one in play holding it."""
    pokemon = ctx.source
    return (ctx.energy_receiver is pokemon and ctx.attached_energy.parent is pokemon
            and pokemon in ctx.board.pokemon_in_play(ctx.player_id))


def _draw_applies(ctx) -> bool:
    # The draw names no Pokemon, so it happens even after the holder
    # evolved first (Solar Evolution) -- only a deck is needed.
    return _this_card_from_hand(ctx) and bool(ctx.deck())


async def draw_energy(ctx):
    """Attached from hand: draw a card."""
    if _draw_applies(ctx):
        await ctx.draw_cards(1)


card = EnergyCardDef(
    guid="2320a5dd-5e0b-5dae-8de2-cf55fe42b9db",
    key="SM12",
    name="Draw Energy",
    display_name="Draw Energy",
    searchable_by=["Draw Energy", "Special", "DrawEnergy"],
    subtypes=["Special"],
    collector_number=209,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    granted_abilities=[
        Ability(
            title="Draw Energy",
            game_text="When you attach this card from your hand to a Pok\u00e9mon, draw a card.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=draw_energy,
            trigger_applies=_draw_applies,
        ),
    ],
)
