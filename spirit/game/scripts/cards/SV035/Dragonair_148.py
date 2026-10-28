"""Dragonair (SV035 148 -- JP SV2a 148; English MEW/148, MEW/181). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="9b0f5624-f6bc-5dfb-be6d-bcdb26ce20e6",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    display_name="Dragonair",
    searchable_by=["Dragonair", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=148,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    family_id=147,
    abilities=[
        Attack(
            title="Beat",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Aqua Slash",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=90,
            effect=_hit_then_lock,
        ),
    ],
)
