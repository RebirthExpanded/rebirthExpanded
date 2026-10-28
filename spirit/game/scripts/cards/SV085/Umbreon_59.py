"""Umbreon (SV085 59 -- JP SV3 070; English OBF/130, PRE/59). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


async def feint_attack(ctx):
    pool = ctx.opponent_pokemon_in_play()
    target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon") if pool else None
    if target is not None:
        await ctx.deal_damage(50, target=target, ignore_weakness=True, ignore_resistance=True, ignore_target_effects=True)


card = PokemonCardDef(
    guid="ee42e2e1-d11f-572b-a4ac-06e6e93dfa19",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name",
    display_name="Umbreon",
    searchable_by=["Umbreon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="SV085",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Feint Attack",
            game_text="This attack does 50 damage to 1 of your opponent's Pokémon. This attack's damage isn't affected by Weakness or Resistance, or by any effects on that Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=feint_attack,
        ),
        Attack(
            title="Pitch-Black Blade",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=_hit_then_lock,
        ),
    ],
)
