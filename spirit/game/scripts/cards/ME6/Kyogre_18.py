"""Kyogre (ME6 18 -- JP M6 018; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _legendary_stadium(board) -> bool:
    area = board.find_global_area("activeStadium")
    return any("Legendary" in (getattr(def_for(c.archetype_id), "display_name", "") or "")
               for c in (area.children if area else []))


async def raging_whirlpool(ctx):
    await ctx.deal_damage()
    if _legendary_stadium(ctx.board):
        for p in list(ctx.opponent_bench()):
            await ctx.deal_damage(50, target=p)


card = PokemonCardDef(
    guid="545a2536-819d-52c9-ab02-1ef2d7d7365f",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogre.Name",
    display_name="Kyogre",
    searchable_by=["Kyogre", "Basic"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Attack(
            title="Waterfall",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Raging Whirlpool",
            game_text="If a Stadium with \"Legendary\" in its name is in play, this attack also does 50 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=raging_whirlpool,
        ),
    ],
)
