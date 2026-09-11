"""Bronzong (BW - Next Destinies 76/99 -- JP BW3-Bh 040/052, the art here).

Stage 1 Metal Pokemon. HP 110, weakness Fire x2, resistance Psychic -20,
retreat 4.

  Ability  Heal Block  Damage can't be healed from any Pokemon (both
                       yours and your opponent's). (Damage counters can
                       still be moved.)
  Oracle Inflict [MCC] 30+  Does 10 more damage for each card in your
                            opponent's hand.

Heal Block is the plain heal lock: prevents_healing for every Pokemon in
play, both sides, Bronzong included. It stops the heal keyword only --
EffectContext.heal returns 0 -- and the parenthesis is why moving or
removing damage counters (Sinister Hand, Damage Pump) goes through
remove_damage_counters, which no heal lock touches.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import healing_block_passive
from spirit.game.data_utils import Ability, Attack, PokemonCardDef


async def oracle_inflict(ctx):
    """30 + 10 for each card in the opponent's hand."""
    await ctx.deal_damage(30 + 10 * ctx.hand_size(ctx.opponent_id))


card = PokemonCardDef(
    guid="a9a4a3bc-22ed-530e-8ba1-7fa91331158f",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=76,
    set_code="BW4",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=436,
    abilities=[
        Ability(title="Heal Block",
                game_text="Damage can't be healed from any Pokémon (both yours and your opponent's). (Damage counters can still be moved.)",
                passive=healing_block_passive(lambda target, carrier: True)),
        Attack(title="Oracle Inflict",
               game_text="Does 10 more damage for each card in your opponent's hand.",
               cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
               damage=30, damage_operator="+", effect=oracle_inflict),
    ],
)
