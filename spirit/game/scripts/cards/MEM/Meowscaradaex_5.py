"""Meowscarada ex (MEM 5 -- JP MEM 005; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def magical_bullet(ctx):
    await ctx.deal_damage()
    damaged = [p for p in ctx.opponent_bench() if _counters(ctx.board, p) > 0]
    if damaged:
        target = await ctx.choose_pokemon(damaged, "Choose a damaged Benched Pokémon to take 120 damage")
        if target is not None:
            await ctx.deal_damage(120, target=target)


card = PokemonCardDef(
    guid="1e1ea29c-51c5-5f87-95cf-3646104930e3",
    key="MEM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowscaradaex.Name",
    display_name="Meowscarada ex",
    searchable_by=["Meowscarada ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=5,
    set_code="MEM",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Floragato.Name",
    family_id=906,
    abilities=[
        Attack(
            title="Magical Bullet",
            game_text="This attack also does 120 damage to 1 of your opponent's Benched Pokémon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 2},
            damage=120,
            effect=magical_bullet,
        ),
    ],
)
