"""Magnezone (BW - Plasma Storm 46/135 -- JP BW7-B 025/070).

Stage 2 Lightning Pokemon, evolves from Magneton. HP 140, weakness
Fighting x2, retreat 3.

  Ability  Dual Brains  During your turn, you may play 2 Supporter cards.
  Gyro Ball  [LLC] 80  Switch this Pokemon with 1 of your Benched Pokemon.
                       Then, your opponent switches the Defending Pokemon
                       with 1 of their Benched Pokemon.

Dual Brains is a new passive hook: the turn's Supporter limit was a bare
flag, and is now a count checked against the largest limit any passive
names, with the rule's own 1 as the floor -- two Magnezone do not make 3.

Gyro Ball switches in order: yours first, theirs second, each only with a
Bench to switch to, and THEY pick their new Active.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.passives import Passive


class DualBrainsPassive(Passive):
    def supporter_play_limit(self, player_id, carrier):
        return 2 if carrier.owning_player_id == player_id else 0


async def gyro_ball(ctx):
    """80, you switch out, then they switch out."""
    await ctx.deal_damage()
    mine = list(ctx.my_bench())
    if mine:
        target = await ctx.choose_pokemon(mine, "Choose your new Active Pokémon")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)
    theirs = list(ctx.opponent_bench())
    defender = ctx.opponent_active()
    if theirs and defender is not None and not ctx.effects_blocked(defender):
        chosen = await ctx.choose_pokemon(
            theirs, "Choose your new Active Pokémon", player_id=ctx.opponent_id)
        if chosen is not None:
            await ctx.switch_active(ctx.opponent_id, chosen)


card = PokemonCardDef(
    guid="b2c916b5-105d-5e28-bf98-dc1a5d462f34",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name",
    display_name="Magnezone",
    searchable_by=["Magnezone", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=46,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    family_id=81,
    abilities=[
        Ability(
            title="Dual Brains",
            game_text="During your turn, you may play 2 Supporter cards.",
            passive=DualBrainsPassive(),
        ),
        Attack(
            title="Gyro Ball",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon. Then, your opponent switches the Defending Pokémon with 1 of their Benched Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=gyro_ball,
        ),
    ],
)
