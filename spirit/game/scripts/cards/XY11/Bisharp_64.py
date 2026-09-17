"""Bisharp (XY - Steam Siege 64/114 -- JP XY11 the art here).

Stage 1 Darkness/Metal Pokemon (Steam Siege dual type). HP 100, weakness
Fighting x2, resistance Psychic -20, retreat 2. Evolves from Pawniard.

  Retaliate  [C] 30+   If any of your Pokemon were Knocked Out by damage
                       from an opponent's attack during their last turn,
                       this attack does 60 more damage.
  Mach Claw  [DC] 60   This attack's damage isn't affected by Resistance.

A dual type is both of its types at once, so under Eternal Zone this is a
Darkness Pokemon and may be put into play (and keeps the zone working).

Retaliate reads kos_by_attack_last_turn -- attack-damage Knock Outs only,
the narrow reading the text asks for (Hisuian Basculegion's shape), not
poison or counters.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.data_utils import Attack, PokemonCardDef


def _ko_by_attack_last_turn(ctx) -> bool:
    return ctx.kos_by_attack_last_turn() > 0


async def mach_claw(ctx):
    """60, Resistance not applied."""
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="afe44ea9-5f63-5131-8e3c-3cf1f2b02a1f",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name",
    display_name="Bisharp",
    searchable_by=["Bisharp", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DARKNESS, PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name",
    family_id=624,
    abilities=[
        Attack(
            title="Retaliate",
            game_text="If any of your Pokémon were Knocked Out by damage from an opponent's attack during their last turn, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(_ko_by_attack_last_turn, 60),
        ),
        Attack(
            title="Mach Claw",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=mach_claw,
        ),
    ],
)
