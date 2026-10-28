"""Magmortar (SV045 10 -- JP SVEL 002; English PAF/10). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="4d20b267-711c-514b-84e7-3e6eb3459c55",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmortar.Name",
    display_name="Magmortar",
    searchable_by=["Magmortar", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    family_id=240,
    abilities=[
        Attack(
            title="Flare",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
        ),
        Attack(
            title="Volcanic Heat",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=_hit_then_lock,
        ),
    ],
)
