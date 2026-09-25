"""Professor Kukui (SM - Sun & Moon 128/149 -- JP SM1S 059/060).

Supporter.

  "Draw 2 cards. During this turn, your Pokemon's attacks do 20 more
   damage to your opponent's Active Pokemon (before applying Weakness and
   Resistance)."

The same turn-long modifier as Leon's +30.
"""

from spirit.game.attributes import Rarities
from spirit.game.session.passives import TurnDamageModifier
from spirit.game.data_utils import SupporterCardDef


async def professor_kukui(ctx):
    await ctx.draw_cards(2)
    ctx.add_turn_damage_modifier(TurnDamageModifier(20, ctx.player_id))
    for pokemon in ctx.my_pokemon_in_play():
        await ctx.add_stat_visualization(
            pokemon, "Positive", "DamageDealtIncreased", card_text="+20 damage"
        )


card = SupporterCardDef(
    guid="b4e84e19-d7a5-554d-a75f-f3b12bfa0319",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorKukui.Name",
    display_name="Professor Kukui",
    searchable_by=["Professor Kukui", "Supporter", "ProfessorKukui"],
    subtypes=["Supporter"],
    collector_number=128,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=professor_kukui,
)
