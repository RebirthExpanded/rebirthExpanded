"""Paldean Student (SV045 85 -- JP SV4a 178; English PAF/230, PAF/231, PAF/85, PAF/86). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.data_utils import def_for, subtypes_for

from spirit.game.session.effects import is_pokemon_card

_RULE_BOX = {"ex", "V", "VMAX", "VSTAR", "V-UNION", "GX", "EX", "Prism Star", "Radiant", "BREAK", "LEGEND", "SV_Mega", "MEGA"}


def _no_rule_box(card) -> bool:
    return is_pokemon_card(card) and not (set(subtypes_for(card.archetype_id) or []) & _RULE_BOX)


async def paldean_student(ctx):
    n = 1 + sum(1 for c in ctx.discard_pile()
                if getattr(def_for(c.archetype_id), "display_name", "") == "Paldean Student" and c is not ctx.source)
    picks = await ctx.search_deck(_no_rule_box, count=n, minimum=0, prompt=f"Choose up to {n} Pokémon without a Rule Box.")
    if picks:
        await ctx.put_in_hand(picks)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="d3a203a4-0d99-5c89-b3cd-ea3e9711c39c",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PaldeanStudent.Name",
    display_name="Paldean Student",
    searchable_by=["Paldean Student", "Supporter"],
    subtypes=["Supporter"],
    collector_number=85,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    effect=paldean_student,
)
