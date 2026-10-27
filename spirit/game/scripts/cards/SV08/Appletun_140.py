"""Appletun (SV08 140 -- JP SV7a 047; English SSP/140, SSP/211). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock_defender(ctx):
    await ctx.deal_damage()
    ac.lock_defender_attacks(ctx)
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="7002c906-4b83-5e54-9801-a241d0a42495",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Appletun.Name",
    display_name="Appletun",
    searchable_by=["Appletun", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=140,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    family_id=840,
    abilities=[
        Attack(
            title="Melting Sweetness",
            game_text="During your opponent's next turn, the Defending Pokémon can't attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=_hit_then_lock_defender,
        ),
        Attack(
            title="Wild Tackle",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1},
            damage=130,
            effect=ac.recoil_attack(20),
        ),
    ],
)
