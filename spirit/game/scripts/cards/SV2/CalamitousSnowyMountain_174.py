"""Calamitous Snowy Mountain (SV - Paldea Evolved 174/193 -- JP SV2P 070/071).

Stadium.

  "Whenever any player attaches an Energy card from their hand to 1 of
   their Basic non-[W] Pokemon, put 2 damage counters on that Pokemon."

Old Cemetery's watch with the Basic non-[W] gate. It runs as the
attaching player and declares trigger_applies, so with Medical Energy's
heal on the same attachment the attaching player picks the order.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import Ability, StadiumCardDef, Triggers
from spirit.game.session.effects import is_basic_pokemon, is_pokemon_of_type


def _snowy_mountain_applies(ctx) -> bool:
    receiver = ctx.energy_receiver
    if receiver is None or receiver.owning_player_id is None:
        return False
    if receiver not in ctx.board.pokemon_in_play(receiver.owning_player_id):
        return False
    if receiver.owning_player_id != ctx.attaching_player_id:
        return False
    return is_basic_pokemon(receiver) and not is_pokemon_of_type(receiver, PokemonTypes.WATER)


async def calamitous_snowy_mountain(ctx):
    """2 damage counters on the Basic non-[W] Pokemon just given an Energy
    card from hand."""
    if _snowy_mountain_applies(ctx):
        await ctx.deal_damage(20, target=ctx.energy_receiver, apply_modifiers=False,
                              as_counters=True)


card = StadiumCardDef(
    guid="9a61761c-de0e-5ca3-9f8d-2591cec41a10",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CalamitousSnowyMountain.Name",
    display_name="Calamitous Snowy Mountain",
    searchable_by=["Calamitous Snowy Mountain", "Stadium", "CalamitousSnowyMountain"],
    subtypes=["Stadium"],
    collector_number=174,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    abilities=[Ability(
        title="Calamitous Snowy Mountain",
        game_text="Whenever any player attaches an Energy card from their hand to 1 of their Basic non-Water Pok\u00e9mon, put 2 damage counters on that Pok\u00e9mon.",
        trigger=Triggers.ON_ENERGY_ATTACHED,
        effect=calamitous_snowy_mountain,
        trigger_applies=_snowy_mountain_applies,
    )],
)
