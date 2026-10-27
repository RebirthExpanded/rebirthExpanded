"""Reboot Pod (SV05 158 -- JP SV5M 063; English TEF/158). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import def_for, subtypes_for


def _has_sub(card, sub) -> bool:
    return card is not None and sub in (subtypes_for(card.archetype_id) or [])


async def reboot_pod(ctx):
    for p in list(ctx.my_pokemon_in_play()):
        if not _has_sub(p, "Future"):
            continue
        pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        if not pool:
            break
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Energy card to attach")
        if picks:
            await ctx.attach_energy(picks[0], p)


card = ItemCardDef(
    guid="bcf57281-83f4-50a2-ad22-a985d5a0d438",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RebootPod.Name",
    display_name="Reboot Pod",
    searchable_by=["Reboot Pod", "Item", "Future", "ACE SPEC"],
    subtypes=["Item", "Future", "ACE SPEC"],
    collector_number=158,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    effect=reboot_pod,
)
