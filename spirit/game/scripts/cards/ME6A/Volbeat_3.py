"""Volbeat (JP M6a 003/103 -- 30th Celebrations; English 30C 3).
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import _gust


async def luring_glow(ctx):
    """Switch in 1 of the opponent's Benched Pokemon to the Active Spot."""
    if ctx.opponent_bench():
        await _gust(ctx)

card = PokemonCardDef(
    guid="911a7da9-8f6b-585f-b8e4-233ed2b83af0",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volbeat.Name",
    display_name="Volbeat",
    searchable_by=["Volbeat", "Basic", "Volbeat"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=313,
    abilities=[
        Attack(
            title="Luring Glow",
            game_text="Switch in 1 of your opponent's Benched Pok\u00e9mon to the Active Spot.",
            cost={PokemonTypes.GRASS: 1},
            damage=0,
            effect=luring_glow,
        ),
        Attack(
            title="Bug Buzz",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)
