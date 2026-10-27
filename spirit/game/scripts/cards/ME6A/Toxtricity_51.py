"""Toxtricity (ME6A 51 -- JP M6a 051; English 30C/134, 30C/60). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="f8027cfd-375e-5ea0-8b97-e3b283c74365",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricity.Name",
    display_name="Toxtricity",
    searchable_by=["Toxtricity", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    family_id=848,
    abilities=[
        Attack(
            title="Light Punch",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=40,
        ),
        Attack(
            title="Thunderous Bolt",
            game_text="During your next turn, this Pokémon can't use attacks.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=_hit_then_lock,
        ),
    ],
)
