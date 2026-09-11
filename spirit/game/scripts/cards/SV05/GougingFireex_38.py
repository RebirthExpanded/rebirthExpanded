"""Gouging Fire ex (SV - Temporal Forces 38/162 -- JP SV5K 012/071).

Basic Fire Pokemon ex (Ancient). HP 230, weakness Water x2, retreat 2.

  Heat Blast   [RC] 60
  Blaze Blitz  [RRC] 260  This Pokemon can't use Blaze Blitz again until
                          it leaves the Active Spot.

The lock is an attack lock that never expires on its own; leaving the
Active Spot clears it (clear_pokemon_effects).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.legal_actions import LOCK_UNTIL_LEAVES_ACTIVE


async def blaze_blitz(ctx):
    await ctx.deal_damage()
    ctx.session.turn_state.attack_locks[(ctx.attacker.entity_id, ctx.ability.ability_id)] = \
        LOCK_UNTIL_LEAVES_ACTIVE


card = PokemonCardDef(
    guid="49e07e5c-5a39-5a8d-975f-0d9f53aae862",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GougingFireex.Name",
    display_name="Gouging Fire ex",
    searchable_by=["Gouging Fire ex", "Basic", "ex", "Ancient", "GougingFireex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=38,
    set_code="SV05",
    rarity=Rarities.RareUltra,
    hp=230,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=1020,
    regulation_mark="H",
    abilities=[
        Attack(title="Heat Blast", game_text="",
               cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1}, damage=60),
        Attack(title="Blaze Blitz",
               game_text="This Pokémon can't use Blaze Blitz again until it leaves the Active Spot.",
               cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1}, damage=260,
               effect=blaze_blitz),
    ],
)
