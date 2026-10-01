"""Jet Energy (SV - Paldea Evolved 190/193 -- JP SV1a 072/073).

Special Energy.  "As long as this card is attached to a Pokemon, it
provides [C] Energy. When you attach this card from your hand to 1 of your
Benched Pokemon, switch that Pokemon with your Active Pokemon."

The switch is an ON_ENERGY_ATTACHED trigger the card grants its holder
(like Medical Energy's heal), so it is ordered with the other triggers of
the same attachment by the holder's owner: Skiploom's Solar Evolution
first and the Pokemon it was attached to is gone -- no switch (ruling).
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.data_utils import Ability, EnergyCardDef, Triggers, def_for
from spirit.game.session.effects import special_energy_neutralized


NAME = "Jet Energy"


def _jet_applies(ctx) -> bool:
    """This Jet Energy, just attached from my hand to this Pokemon, which is
    still on my Bench."""
    energy = ctx.attached_energy
    if energy is None or getattr(def_for(energy.archetype_id), "display_name", None) != NAME:
        return False
    if ctx.attaching_player_id != ctx.player_id or ctx.energy_receiver is not ctx.source:
        return False
    pokemon = ctx.source
    if energy.parent is not pokemon or special_energy_neutralized(energy):
        return False
    return (pokemon in ctx.board.pokemon_in_play(ctx.player_id)
            and not is_in_active_spot(pokemon))


async def jet_energy(ctx):
    if _jet_applies(ctx):
        await ctx.switch_active(ctx.player_id, ctx.source)


card = EnergyCardDef(
    guid="ef988193-5321-5dfb-8a2a-4fc795195e22",
    key="SV2",
    name="Jet Energy",
    display_name="Jet Energy",
    searchable_by=["Jet Energy", "Special", "JetEnergy"],
    subtypes=["Special"],
    collector_number=190,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    regulation_mark="G",
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    granted_abilities=[
        Ability(
            title="Jet Energy",
            game_text="When you attach this card from your hand to 1 of your Benched Pokémon, switch that Pokémon with your Active Pokémon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=jet_energy,
            trigger_applies=_jet_applies,
        ),
    ],
)
