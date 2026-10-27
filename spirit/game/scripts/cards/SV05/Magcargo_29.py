"""Magcargo (SV05 29 -- JP SV5M 018; English TEF/29). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


def _lava_zone_applies(ctx) -> bool:
    moved = getattr(ctx, "moved_pokemon", None)
    return moved is not None and moved.owning_player_id != ctx.source.owning_player_id


async def lava_zone(ctx):
    if ctx.moved_pokemon is not None:
        await ctx.apply_special_condition(ctx.moved_pokemon, SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="3060376d-b1a5-5b0d-9ed0-f34b3488ca96",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magcargo.Name",
    display_name="Magcargo",
    searchable_by=["Magcargo", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    family_id=218,
    abilities=[
        Ability(
            title="Lava Zone",
            game_text="Whenever your opponent's Active Pokémon moves to the Bench during their turn, their new Active Pokémon is now Burned.",
            trigger=Triggers.ON_OPPONENT_MOVE_TO_ACTIVE,
            trigger_applies=_lava_zone_applies,
            effect=lava_zone,
        ),
        Attack(
            title="Heat Blast",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
