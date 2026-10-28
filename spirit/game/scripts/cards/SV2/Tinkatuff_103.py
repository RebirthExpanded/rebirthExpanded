"""Tinkatuff (SV2 103 -- JP SV1a 042; English PAL/103). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="21ba0d1c-ffa7-5ec8-ae69-1f38987ea692",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name",
    display_name="Tinkatuff",
    searchable_by=["Tinkatuff", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=103,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatink.Name",
    family_id=957,
    abilities=[
        Attack(
            title="Light Punch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Boundless Power",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=_hit_then_lock,
        ),
    ],
)
