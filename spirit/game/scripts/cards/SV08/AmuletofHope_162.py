"""Amulet of Hope (SV08 162 -- JP SV8 098; English SSP/162). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef

from spirit.game.data_utils import Ability, Triggers


def _amulet_applies(ctx) -> bool:
    attacker = getattr(ctx, "ko_attacker", None)
    return (bool(getattr(ctx, "ko_from_attack", False)) and attacker is not None
            and attacker.owning_player_id != ctx.source.owning_player_id)


async def _amulet_of_hope(ctx):
    picks = await ctx.search_deck(count=3, minimum=0, prompt="Choose up to 3 cards to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonToolCardDef(
    guid="a0046cfa-e705-5b89-92a4-a851424fb2b6",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AmuletofHope.Name",
    display_name="Amulet of Hope",
    searchable_by=["Amulet of Hope", "Pokémon Tool", "ACE SPEC"],
    subtypes=["Pokémon Tool", "ACE SPEC"],
    collector_number=162,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    granted_abilities=[
        Ability(
            title="Amulet of Hope",
            game_text="If the Pokémon this card is attached to is Knocked Out by damage from an attack from your opponent's Pokémon, search your deck for up to 3 cards and put them into your hand. Then, shuffle your deck.",
            trigger=Triggers.ON_KNOCKED_OUT,
            trigger_applies=_amulet_applies,
            effect=_amulet_of_hope,
        ),
    ],
)
