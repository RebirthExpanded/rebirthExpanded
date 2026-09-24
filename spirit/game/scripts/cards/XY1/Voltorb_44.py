"""Voltorb (XY - XY 44/146 -- JP XY1 021/060, the art here).

Basic Lightning Pokemon. HP 50, weakness Fighting x2, retreat 1.

  Destiny Burst  (Ability)  If this Pokemon is your Active Pokemon and is
                            Knocked Out by damage from an opponent's
                            attack, flip a coin. If heads, put 5 damage
                            counters on the Attacking Pokemon.
  Rollout        [L] 10

ON_KNOCKED_OUT_IN_PLAY (the Batons' trigger), so the flip happens while
the KO'd stack is still on the board and the attacker is still there to
take the counters.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers

COUNTERS = 5


async def destiny_burst(ctx):
    if not (ctx.ko_from_attack and ctx.was_active_at_ko):
        return
    attacker = ctx.ko_attacker
    if attacker is None or attacker.owning_player_id == ctx.player_id:
        return
    if not (await ctx.flip_coins(1, "Destiny Burst"))[0]:
        return
    await ctx.deal_damage(COUNTERS * 10, target=attacker,
                          apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="4c47f5f1-5375-5dc3-b300-3d692c52d557",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    display_name="Voltorb",
    searchable_by=["Voltorb", "Basic"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="XY1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=100,
    abilities=[
        Ability(
            title="Destiny Burst",
            game_text="If this Pokémon is your Active Pokémon and is Knocked Out by damage from an opponent's attack, flip a coin. If heads, put 5 damage counters on the Attacking Pokémon.",
            trigger=Triggers.ON_KNOCKED_OUT_IN_PLAY,
            effect=destiny_burst,
        ),
        Attack(
            title="Rollout",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)
