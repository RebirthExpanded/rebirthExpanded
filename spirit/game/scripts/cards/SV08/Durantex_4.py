"""Durant ex (SV - Surging Sparks 4/191 -- JP SV8 003/106, the art here).

Basic Grass Pokemon ex. HP 190, weakness Fire x2, no resistance, retreat 2.

  Ability  Sudden Shearing  When you play this Pokemon from your hand onto
                            your Bench during your turn, you may discard
                            the top card of your opponent's deck.
  Vengeful Crush [GCC] 120+  This attack does 30 more damage for each
                             Prize card your opponent has taken.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_prizes_taken, damage_per
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers


async def sudden_shearing(ctx):
    top = ctx.deck_top(1, player_id=ctx.opponent_id)
    if not top:
        return
    if await ctx.ask_yes_no("Discard the top card of your opponent's deck?"):
        await ctx.discard_cards(top)


card = PokemonCardDef(
    guid="7b1e95b4-8031-58d6-a40d-6e14ebfbfa27",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Durantex.Name",
    display_name="Durant ex",
    searchable_by=["Durant ex", "Basic", "ex", "Durantex"],
    subtypes=["Basic", "ex"],
    collector_number=4,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=632,
    abilities=[
        Ability(title="Sudden Shearing",
                game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may discard the top card of your opponent's deck.",
                trigger=Triggers.ON_PLAY, effect=sudden_shearing),
        Attack(title="Vengeful Crush",
               game_text="This attack does 30 more damage for each Prize card your opponent has taken.",
               cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
               damage=120, damage_operator="+",
               effect=damage_per(count_prizes_taken("opponent"), 30, base=120)),
    ],
)
