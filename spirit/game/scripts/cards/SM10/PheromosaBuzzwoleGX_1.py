"""Pheromosa & Buzzwole-GX (SM - Unbroken Bonds 1/214 -- JP SM9b 001/054,
the art here).

Basic Grass TAG TEAM Pokemon-GX, Ultra Beast. HP 260, weakness Fire x2,
retreat 2.

  Jet Punch     [G]   30  30 damage to 1 of your opponent's Benched Pokemon.
  Elegant Sole  [GGC] 190  During your next turn, this Pokemon's Elegant
                           Sole attack's base damage is 60.
  Beast Game-GX [G+]  50  If your opponent's Pokemon is Knocked Out by
                          damage from this attack, take 1 more Prize card.
                          If this Pokemon has at least 7 extra Energy
                          attached to it (in addition to this attack's
                          cost), take 3 more Prize cards instead.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import apply_own_next_turn_boost
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.legal_actions import attack_cost_satisfied

_BEAST_GAME_PLUS_7 = {"Grass": 1, "Colorless": 7}


async def jet_punch(ctx):
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    if bench:
        target = await ctx.choose_pokemon(
            bench, "Choose 1 of your opponent's Benched Pokémon") or bench[0]
        await ctx.deal_damage(30, target=target)


async def elegant_sole(ctx):
    await ctx.deal_damage()
    # "base damage is 60" next turn: 190 - 130.
    await apply_own_next_turn_boost(ctx, -130, "Elegant Sole")


async def beast_game_gx(ctx):
    big = attack_cost_satisfied(_BEAST_GAME_PLUS_7, ctx.attached_energies(ctx.attacker), ctx.board)
    defender = ctx.defender
    await ctx.deal_damage()
    if defender is not None and defender in ctx.knockouts:
        ctx.extra_prizes += 3 if big else 1


card = PokemonCardDef(
    guid="9f87d219-199b-52f3-bb20-b91972b08852",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PheromosaBuzzwoleGX.Name",
    display_name="Pheromosa & Buzzwole-GX",
    searchable_by=["Pheromosa & Buzzwole-GX", "Basic", "TAG TEAM", "GX", "Ultra Beast",
                   "PheromosaBuzzwoleGX"],
    subtypes=["Basic", "TAG TEAM", "GX", "Ultra Beast"],
    collector_number=1,
    set_code="SM10",
    rarity=Rarities.RareHoloGX,
    hp=260,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=795,
    abilities=[
        Attack(
            title="Jet Punch",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=jet_punch,
        ),
        Attack(
            title="Elegant Sole",
            game_text="During your next turn, this Pokémon's Elegant Sole attack's base damage is 60.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=elegant_sole,
        ),
        Attack(
            title="Beast Game-GX",
            game_text="If your opponent's Pokémon is Knocked Out by damage from this attack, take 1 more Prize card. If this Pokémon has at least 7 extra Energy attached to it (in addition to this attack's cost), take 3 more Prize cards instead. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            gx=True,
            effect=beast_game_gx,
        ),
    ],
)
