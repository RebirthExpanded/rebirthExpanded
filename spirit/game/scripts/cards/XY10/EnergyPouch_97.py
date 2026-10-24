"""Energy Pouch (XY - BREAKpoint 97/122).

Pokemon Tool.

  "If the Pokemon this card is attached to is Knocked Out by damage from an
   opponent's attack, put all basic Energy attached to that Pokemon into
   your hand."

ON_KNOCKED_OUT_IN_PLAY (Wishful Baton's hook): it runs before the stack
moves, so the basic Energy is still attached and goes straight to the hand.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import Ability, PokemonToolCardDef, Triggers


async def energy_pouch(ctx):
    if not ctx.ko_from_attack:
        return
    pool = [e for e in ctx.attached_energies(ctx.source) if is_basic_energy_card(e)]
    if pool:
        await ctx.put_in_hand(pool)


card = PokemonToolCardDef(
    guid="8067bf07-1cd5-588d-b3b2-dfd6ab99c2ff",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyPouch.Name",
    display_name="Energy Pouch",
    searchable_by=["Energy Pouch", "Pokémon Tool", "EnergyPouch"],
    subtypes=["Pokémon Tool"],
    collector_number=97,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Energy Pouch",
            game_text="If the Pokémon this card is attached to is Knocked Out by damage from an opponent's attack, put all basic Energy attached to that Pokémon into your hand.",
            trigger=Triggers.ON_KNOCKED_OUT_IN_PLAY,
            effect=energy_pouch,
            trigger_applies=lambda c: bool(c.ko_from_attack),
        ),
    ],
)
