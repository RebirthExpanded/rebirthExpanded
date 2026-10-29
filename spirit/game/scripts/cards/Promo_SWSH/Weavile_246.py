"""Weavile (Promo_SWSH 246 -- JP SP 261; English SP/246). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID


async def _pursuit_claw(ctx):
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your opponent's Benched Pokémon")
    if target is None:
        return
    counters = max(0, (ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0)) // 10)
    if counters:
        await ctx.deal_damage(20 * counters, target=target, apply_modifiers=False)


card = PokemonCardDef(
    guid="dca21dfa-195d-5a3f-b4a1-2c0665837da4",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weavile.Name",
    display_name="Weavile",
    searchable_by=["Weavile", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=246,
    set_code="Promo_SWSH",
    regulation_mark="F",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    family_id=215,
    abilities=[
        Attack(
            title="Pursuit Claw",
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pokémon for each damage counter on that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 1},
            effect=_pursuit_claw,
        ),
        Attack(
            title="Claw Slash",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)
