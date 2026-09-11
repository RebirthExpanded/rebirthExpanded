"""Reshiram & Charizard-GX (SM - Unbroken Bonds 20/214 -- JP SM10 007/095).

Basic Fire TAG TEAM Pokemon-GX. HP 270, weakness Water x2, retreat 3.

  Outrage       [RC] 30+   This attack does 10 more damage for each damage
                           counter on this Pokemon.
  Flare Strike  [RRRC] 230  This Pokemon can't use Flare Strike during
                            your next turn.
  Double Blaze-GX  [RRR+] 200+  If this Pokemon has at least 3 extra [R]
                   Energy attached to it (in addition to this attack's
                   cost), this attack does 100 more damage, and this
                   attack's damage isn't affected by any effects on your
                   opponent's Active Pokemon.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on, damage_per
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.legal_actions import attack_cost_satisfied

_COST_PLUS_EXTRA = {"Fire": 6}


async def flare_strike(ctx):
    await ctx.deal_damage()
    ctx.session.turn_state.lock_attack(ctx.attacker.entity_id, ctx.ability.ability_id)


async def double_blaze_gx(ctx):
    energies = ctx.attached_energies(ctx.attacker)
    if attack_cost_satisfied(_COST_PLUS_EXTRA, energies, ctx.board):
        await ctx.deal_damage(300, ignore_target_effects=True)
    else:
        await ctx.deal_damage(200)


card = PokemonCardDef(
    guid="78ea1ec4-5391-5916-8722-083bdfd7b5da",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ReshiramCharizardGX.Name",
    display_name="Reshiram & Charizard-GX",
    searchable_by=["Reshiram & Charizard-GX", "Basic", "TAG TEAM", "GX", "ReshiramCharizardGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=20,
    set_code="SM10",
    rarity=Rarities.RareHoloGX,
    hp=270,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=643,
    abilities=[
        Attack(title="Outrage",
               game_text="This attack does 10 more damage for each damage counter on this Pokémon.",
               cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1}, damage=30,
               effect=damage_per(damage_counters_on("self"), 10, base=30)),
        Attack(title="Flare Strike",
               game_text="This Pokémon can't use Flare Strike during your next turn.",
               cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1}, damage=230,
               effect=flare_strike),
        Attack(title="Double Blaze-GX",
               game_text="If this Pokémon has at least 3 extra [R] Energy attached to it (in addition to this attack's cost), this attack does 100 more damage, and this attack's damage isn't affected by any effects on your opponent's Active Pokémon. (You can't use more than 1 GX attack in a game.)",
               cost={PokemonTypes.FIRE: 3}, damage=200, gx=True,
               effect=double_blaze_gx),
    ],
)
