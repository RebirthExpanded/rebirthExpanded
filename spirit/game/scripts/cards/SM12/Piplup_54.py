"""Piplup (SM - Cosmic Eclipse 54/236 -- JP SM11b 009/049).

Basic Water Pokemon. HP 60, weakness Lightning x2, retreat 1.

  Bubble Hold  [WWW] 80  If the Defending Pokemon is a Basic Pokemon, it
                         can't attack during your opponent's next turn.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import lock_defender_attacks
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.data_utils import Attack, PokemonCardDef


async def bubble_hold(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and defender not in ctx.knockouts and is_basic_pokemon(defender):
        lock_defender_attacks(ctx, defender)


card = PokemonCardDef(
    guid="92b8eb0e-d97e-5e69-9115-e8fddaf60677",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Piplup.Name",
    display_name="Piplup",
    searchable_by=['Piplup', 'Basic', 'Piplup'],
    subtypes=['Basic'],
    collector_number=54,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=393,
    abilities=[
        Attack(title="Bubble Hold", game_text="If the Defending Pokémon is a Basic Pokémon, it can't attack during your opponent's next turn.",
               cost={PokemonTypes.WATER: 3}, damage=80,
               effect=bubble_hold),
    ],
)
