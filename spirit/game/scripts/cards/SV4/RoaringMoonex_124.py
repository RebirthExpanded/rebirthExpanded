"""Roaring Moon ex (SV - Paradox Rift 124/182 -- JP SV4K 054/066).

Basic Darkness Pokemon ex (Ancient). HP 230, weakness Grass x2, retreat 2.

  Frenzied Gouging  [DDC]  Knock Out your opponent's Active Pokemon. If
                           your opponent's Active Pokemon is Knocked Out
                           in this way, this Pokemon does 200 damage to
                           itself.
  Calamity Storm  [DDC] 100+  You may discard a Stadium in play. If you
                              do, this attack does 120 more damage.

The Knock Out is an attack EFFECT (a shielded Active stays), and the
self-damage is damage from this Pokemon's own attack, which is what
Protection Cube prevents.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef


async def frenzied_gouging(ctx):
    if await ctx.knock_out(ctx.opponent_active()):
        await ctx.deal_damage(200, target=ctx.attacker, apply_modifiers=False)


async def calamity_storm(ctx):
    bonus = 0
    if ctx.stadium_in_play() is not None and await ctx.ask_yes_no(
            "Discard the Stadium in play for 120 more damage?"):
        if await ctx.discard_stadium() is not None:
            bonus = 120
    await ctx.deal_damage(100 + bonus)


card = PokemonCardDef(
    guid="40c268dc-1150-59ba-86fb-66ab9c6145d5",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RoaringMoonex.Name",
    display_name="Roaring Moon ex",
    searchable_by=["Roaring Moon ex", "Basic", "ex", "Ancient", "RoaringMoonex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=124,
    set_code="SV4",
    rarity=Rarities.RareUltra,
    hp=230,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=1005,
    regulation_mark="G",
    abilities=[
        Attack(
            title="Frenzied Gouging",
            game_text="Knock Out your opponent's Active Pokémon. If your opponent's Active Pokémon is Knocked Out in this way, this Pokémon does 200 damage to itself.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=0,
            effect=frenzied_gouging,
        ),
        Attack(
            title="Calamity Storm",
            game_text="You may discard a Stadium in play. If you do, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=calamity_storm,
        ),
    ],
)
