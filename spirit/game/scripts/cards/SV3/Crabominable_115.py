"""Crabominable (SV3 115 -- JP SV2D 043; English OBF/115). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="766b0a2d-59cb-558c-9371-c841264bb022",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crabominable.Name",
    display_name="Crabominable",
    searchable_by=["Crabominable", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=115,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Crabrawler.Name",
    family_id=739,
    abilities=[
        Attack(
            title="Confront",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Knuckle Impact",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=_hit_then_lock,
        ),
    ],
)
