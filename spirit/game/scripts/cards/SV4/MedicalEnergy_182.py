"""Medical Energy (SV - Paradox Rift 182/182 -- JP SV3a 062/062).

Special Energy.

  "As long as this card is attached to a Pokemon, it provides [C] Energy.
   When you attach this card from your hand to 1 of your Pokemon, heal 30
   damage from that Pokemon."

The heal is an ON_ENERGY_ATTACHED trigger the card grants its holder, so
it sits in the same ordered pool as Calamitous Snowy Mountain's counters
(or Gnawing Curse, Old Cemetery): the attaching player -- the holder's
owner -- picks which resolves first.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import Ability, EnergyCardDef, Triggers, def_for
from spirit.game.session.effects import special_energy_neutralized

NAME = "Medical Energy"


def _medical_applies(ctx) -> bool:
    energy = ctx.attached_energy
    if energy is None or getattr(def_for(energy.archetype_id), "display_name", None) != NAME:
        return False
    if ctx.attaching_player_id != ctx.player_id or ctx.energy_receiver is not ctx.source:
        return False
    if energy.parent is not ctx.source or special_energy_neutralized(energy):
        return False
    return ctx.source in ctx.board.pokemon_in_play(ctx.player_id)


async def medical_energy(ctx):
    """Heal 30 from the Pokemon this card was just attached to from hand."""
    if _medical_applies(ctx):
        await ctx.heal(30, ctx.source)


card = EnergyCardDef(
    guid="a975a1a0-741a-508c-8975-db6c1ae62267",
    key="SV4",
    name="Medical Energy",
    display_name="Medical Energy",
    searchable_by=["Medical Energy", "Special"],
    subtypes=["Special"],
    collector_number=182,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    granted_abilities=[
        Ability(
            title="Medical Energy",
            game_text="When you attach this card from your hand to 1 of your Pok\u00e9mon, heal 30 damage from that Pok\u00e9mon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=medical_energy,
            trigger_applies=_medical_applies,
        ),
    ],
)
