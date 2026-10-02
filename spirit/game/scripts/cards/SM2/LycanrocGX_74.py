"""Lycanroc-GX (SM - Guardians Rising 74/145 -- JP SM8b 060/150, the art here).

Stage 1 Fighting Pokemon-GX, evolves from Rockruff. HP 200, weakness Grass
x2, retreat 2.

  Ability: Bloodthirsty Eyes  When you play this Pokemon from your hand to
                              evolve 1 of your Pokemon during your turn,
                              you may switch 1 of your opponent's Benched
                              Pokemon with their Active Pokemon.
  Claw Slash          [FCC] 110
  Dangerous Rogue-GX  [FC]  50x  50 damage for each of your opponent's
                                 Benched Pokemon.

Bloodthirsty Eyes declares trigger_applies, so it is ordered with Po
Town's counters by Lycanroc-GX's owner; with Mimikyu's Shadow Box in play,
the counters first leave it without Abilities (official Q&A).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers


def _bloodthirsty_applies(ctx) -> bool:
    return (getattr(ctx, "evolved_from_hand", False)
            and ctx.session.turn_state.active_player_id == ctx.player_id
            and bool(ctx.opponent_bench()))


async def bloodthirsty_eyes(ctx):
    if not _bloodthirsty_applies(ctx):
        return
    if not await ctx.ask_yes_no("Use Bloodthirsty Eyes to switch in 1 of your opponent's Benched Pokémon?"):
        return
    bench = ctx.opponent_bench()
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon to switch in") or bench[0]
    await ctx.switch_active(ctx.opponent_id, target)


async def dangerous_rogue_gx(ctx):
    await ctx.deal_damage(50 * len(ctx.opponent_bench()))


card = PokemonCardDef(
    guid="95e0a842-a31e-5405-b0b3-8a61b1cffaa1",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LycanrocGX.Name",
    display_name="Lycanroc-GX",
    searchable_by=["Lycanroc-GX", "Stage 1", "GX", "LycanrocGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=74,
    set_code="SM2",
    rarity=Rarities.RareHoloGX,
    hp=200,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    family_id=744,
    abilities=[
        Ability(
            title="Bloodthirsty Eyes",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may switch 1 of your opponent's Benched Pokémon with their Active Pokémon.",
            trigger=Triggers.ON_EVOLVE,
            effect=bloodthirsty_eyes,
            trigger_applies=_bloodthirsty_applies,
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
        Attack(
            title="Dangerous Rogue-GX",
            game_text="This attack does 50 damage for each of your opponent's Benched Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            gx=True,
            effect=dangerous_rogue_gx,
        ),
    ],
)
