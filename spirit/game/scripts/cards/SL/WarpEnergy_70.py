"""Warp Energy (SM - Shining Legends 70/73 -- JP SM3+ 072/072).

Special Energy.  "This card provides [C] Energy. When you attach this card
from your hand to your Active Pokemon, switch that Pokemon with 1 of your
Benched Pokemon."

Jet Energy (SV2)'s shape turned around: the hand attach to the Active
switches it out, the player choosing the Benched Pokemon. The switch is not
optional; with an empty Bench nothing happens.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.data_utils import Ability, EnergyCardDef, Triggers, def_for
from spirit.game.session.effects import special_energy_neutralized


NAME = "Warp Energy"


def _this_card_from_hand(ctx) -> bool:
    """This Warp Energy, just attached from my hand (and not switched off)."""
    energy = ctx.attached_energy
    if energy is None or getattr(def_for(energy.archetype_id), "display_name", None) != NAME:
        return False
    return ctx.attaching_player_id == ctx.player_id and not special_energy_neutralized(energy)


def _still_on_that_pokemon(ctx) -> bool:
    """...to this Pokemon, which is still the one in play holding it."""
    pokemon = ctx.source
    return (ctx.energy_receiver is pokemon and ctx.attached_energy.parent is pokemon
            and pokemon in ctx.board.pokemon_in_play(ctx.player_id))


def _warp_applies(ctx) -> bool:
    return (_this_card_from_hand(ctx) and _still_on_that_pokemon(ctx)
            and is_in_active_spot(ctx.source) and bool(ctx.my_bench()))


async def warp_energy(ctx):
    """Attached from hand to my Active: switch it with 1 of my Benched
    Pokemon. Ordered with the attachment's other triggers by its owner."""
    if not _warp_applies(ctx):
        return
    bench = ctx.my_bench()
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to switch in") or bench[0]
    await ctx.switch_active(ctx.player_id, target)


card = EnergyCardDef(
    guid="38967c5d-dd3a-527b-98b2-321714892647",
    key="SL",
    name="Warp Energy",
    display_name="Warp Energy",
    searchable_by=["Warp Energy", "Special", "WarpEnergy"],
    subtypes=["Special"],
    collector_number=70,
    set_code="SL",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    granted_abilities=[
        Ability(
            title="Warp Energy",
            game_text="When you attach this card from your hand to your Active Pok\u00e9mon, switch that Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=warp_energy,
            trigger_applies=_warp_applies,
        ),
    ],
)
