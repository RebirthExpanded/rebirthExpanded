"""Heavy Baton (SV - Temporal Forces 151/162 -- JP SV5M 066/071, the art here).

Pokemon Tool.

  "If the Pokemon this card is attached to has a Retreat Cost of exactly 4,
   is in the Active Spot, and is Knocked Out by damage from an attack from
   your opponent's Pokemon, move up to 3 Basic Energy cards from that
   Pokemon to your Benched Pokemon in any way you like."

ON_KNOCKED_OUT_IN_PLAY: runs while the KO'd stack is still on board, so
the Energy is moved straight off it (each card picks its own bencher).
The Retreat Cost is the effective one at the moment of the KO.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import Ability, PokemonToolCardDef, Triggers
from spirit.game.session.passives import effective_retreat_cost


async def heavy_baton(ctx):
    holder = ctx.source
    if not ctx.ko_from_attack or not ctx.was_active_at_ko:
        return
    if effective_retreat_cost(ctx.board, holder) != 4:
        return
    bench = ctx.my_bench()
    pool = [e for e in ctx.attached_energies(holder) if is_basic_energy_card(e)]
    if not bench or not pool:
        return
    picks = await ctx.choose_cards(
        pool, min(3, len(pool)), minimum=0,
        prompt="Choose up to 3 Basic Energy cards to move to your Benched Pokémon")
    for energy in picks:
        target = await ctx.choose_pokemon(
            ctx.my_bench(), "Choose a Benched Pokémon to move the Energy to")
        if target is None:
            target = ctx.my_bench()[0]
        await ctx.move_energy(energy, target)


card = PokemonToolCardDef(
    guid="d7d4c02d-be34-5abc-9af9-3ccf90b373e7",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HeavyBaton.Name",
    display_name="Heavy Baton",
    searchable_by=["Heavy Baton", "Item", "Pokémon Tool", "HeavyBaton"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=151,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Heavy Baton",
            game_text="If the Pokémon this card is attached to has a Retreat Cost of exactly 4, is in the Active Spot, and is Knocked Out by damage from an attack from your opponent's Pokémon, move up to 3 Basic Energy cards from that Pokémon to your Benched Pokémon in any way you like.",
            trigger=Triggers.ON_KNOCKED_OUT_IN_PLAY,
            effect=heavy_baton,
        ),
    ],
)
