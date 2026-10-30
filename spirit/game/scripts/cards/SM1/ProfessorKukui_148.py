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
    guid="30a2b596-dc83-5a33-b1cf-40ba5f7d9405",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorKukui.Name",
    display_name="Professor Kukui",
    searchable_by=["Professor Kukui", "Supporter", "ProfessorKukui"],
    subtypes=["Supporter"],
    collector_number=148,
    set_code="SM1",
    rarity=Rarities.RareUltra,
    effect=professor_kukui,
)
