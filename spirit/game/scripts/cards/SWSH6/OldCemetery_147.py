from spirit.game.data_utils import StadiumCardDef, Ability, Triggers
from spirit.game.attributes import Rarities, AttrID, PokemonTypes


async def old_cemetery_watch(ctx):
    """2 damage counters on any non-Psychic Pokemon an Energy was just
    manually attached to (either player)."""
    if _old_cemetery_applies(ctx):
        await ctx.deal_damage(20, target=ctx.energy_receiver, apply_modifiers=False,
                              as_counters=True)


def _old_cemetery_applies(ctx) -> bool:
    receiver = ctx.energy_receiver
    if receiver is None or receiver.owning_player_id is None:
        return False
    if receiver not in ctx.board.pokemon_in_play(receiver.owning_player_id):
        return False
    types = receiver.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.PSYCHIC.value not in types


card = StadiumCardDef(
    guid="cfa7ff8a-9c7d-5f4e-9ebb-d35870f76f39",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OldCemetery.Name",
    display_name="Old Cemetery",
    searchable_by=["Old Cemetery", "Stadium"],
    subtypes=["Stadium"],
    collector_number=147,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title="Old Cemetery",
            game_text="Whenever any player attaches an Energy card from their hand to 1 of their non-Psychic Pokémon, put 2 damage counters on that Pokémon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=old_cemetery_watch,
            trigger_applies=_old_cemetery_applies,
        ),
    ],
)
