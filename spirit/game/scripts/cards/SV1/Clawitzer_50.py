"""Clawitzer (SV1 50 -- JP SV1V 022; English SVI/50). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="f1ac4133-82f8-5238-8e98-8d238e9f6c1c",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clawitzer.Name",
    display_name="Clawitzer",
    searchable_by=["Clawitzer", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clauncher.Name",
    family_id=692,
    abilities=[
        Attack(
            title="Water Gun",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Aqua Cannon",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=_hit_then_lock,
        ),
    ],
)
