"""Hisuian Zoroark (ME6A 99 -- JP M6a 099; English 30C/123). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


async def swirling_resentment(ctx):
    target = ctx.opponent_active()
    if target is None:
        return
    amount = target.get_attribute(AttrID.HP, 0) - 50
    if amount > 0:
        await ctx.deal_damage(amount, target=target, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="717edeb0-c24a-5761-8eda-3423fe667eeb",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianZoroark.Name",
    display_name="Hisuian Zoroark",
    searchable_by=["Hisuian Zoroark", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=99,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianZorua.Name",
    family_id=570,
    abilities=[
        Attack(
            title="Scratch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Swirling Resentment",
            game_text="Place damage counters on your opponent's Active Pokémon until its remaining HP is 50.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=swirling_resentment,
        ),
    ],
)
