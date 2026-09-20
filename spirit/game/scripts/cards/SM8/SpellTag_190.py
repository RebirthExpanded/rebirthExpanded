"""Spell Tag (SM - Lost Thunder 190/214 -- JP SM7b 044/050, the art here).

Pokemon Tool.

  "If the Pokemon this card is attached to is Knocked Out by damage from
   an opponent's attack, put 4 damage counters on your opponent's Pokemon
   in any way you like."

Wishful Baton's trigger (ON_KNOCKED_OUT_IN_PLAY, pre-discard, no Active
requirement) and the click-to-place picker over the opponent's Pokemon
still in play -- an attacker that fell to the same exchange is no
longer a target.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import Ability, PokemonToolCardDef, Triggers

COUNTERS = 4


async def spell_tag(ctx):
    if not ctx.ko_from_attack:
        return
    await ctx.place_damage_counters(COUNTERS)


card = PokemonToolCardDef(
    guid="2109dc95-17ca-5b87-91b4-b071b1352f1b",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpellTag.Name",
    display_name="Spell Tag",
    searchable_by=["Spell Tag", "Item", "Pokémon Tool", "SpellTag"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=190,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Spell Tag",
            game_text="If the Pokémon this card is attached to is Knocked Out by damage from an opponent's attack, put 4 damage counters on your opponent's Pokémon in any way you like.",
            trigger=Triggers.ON_KNOCKED_OUT_IN_PLAY,
            effect=spell_tag,
        ),
    ],
)
