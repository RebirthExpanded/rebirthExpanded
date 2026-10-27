"""Fraxure (ZSV10PT5 69 -- JP SV11B 071; English BLK/146, BLK/69). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="8816d24c-7150-5738-9dba-cba7c9e9d1d4",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fraxure.Name",
    display_name="Fraxure",
    searchable_by=["Fraxure", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Axew.Name",
    family_id=610,
    abilities=[
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Boundless Power",
            game_text="During your next turn, this Pokémon can't use attacks.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            damage=90,
            effect=_hit_then_lock,
        ),
    ],
)
