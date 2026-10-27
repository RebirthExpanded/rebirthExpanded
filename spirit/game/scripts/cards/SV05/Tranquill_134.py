"""Tranquill (SV05 134 -- JP SV5M 058; English TEF/134). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="6b6abed0-cad9-5642-8876-be74cf0fc888",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tranquill.Name",
    display_name="Tranquill",
    searchable_by=["Tranquill", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=134,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidove.Name",
    family_id=519,
    abilities=[
        Attack(
            title="Speed Dive",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Jet Wing",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=_hit_then_lock,
        ),
    ],
)
