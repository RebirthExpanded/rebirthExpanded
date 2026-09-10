from spirit.game.data_utils import ItemCardDef, has_evolution
from spirit.game.attributes import AttrID, Rarities


def _boost_shake_targets(pokemon_in_play):
    """Pokemon there is something to evolve into. "1 of your Pokemon" has to
    be a Pokemon that can be evolved, so a card that evolves from it must
    exist; with only fully evolved Pokemon in play there is no target, the
    card is unplayable, and the deck is never opened. Wally's gate."""
    return [p for p in pokemon_in_play
            if has_evolution(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME))]


def _boost_shake_condition(board, player_id):
    return bool(_boost_shake_targets(board.pokemon_in_play(player_id)))


async def boost_shake(ctx):
    """Search a card that evolves from 1 of your Pokemon, evolve it immediately, shuffle. Your turn ends."""
    candidates = _boost_shake_targets(ctx.my_pokemon_in_play())
    if candidates:
        target = await ctx.choose_pokemon(candidates, "Choose a Pokémon to evolve")
        logic_name = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) if target else None
        if logic_name:
            picks = await ctx.search_deck(
                lambda c, name=logic_name: c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name,
                count=1, minimum=0,
                prompt="Choose a card that evolves from that Pokémon.",
            )
            if picks:
                await ctx.evolve_pokemon(target, picks[0])
        await ctx.shuffle_deck()
    ctx.ends_turn = True


card = ItemCardDef(
    guid="a364bf94-15e5-548a-8e10-c538dcf29d76",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BoostShake.Name",
    display_name="Boost Shake",
    searchable_by=["Boost Shake", "Item"],
    subtypes=["Item"],
    collector_number=229,
    set_code="SWSH7",
    rarity=Rarities.RareSecret,
    effect=boost_shake,
    condition=_boost_shake_condition,
)
