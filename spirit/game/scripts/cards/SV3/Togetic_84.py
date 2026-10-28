"""Togetic (SV3 84 -- JP SV3 044; English OBF/84). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def shared_peace(ctx):
    await ctx.draw_cards(3)
    await ctx.draw_cards(3, player_id=ctx.opponent_id)


card = PokemonCardDef(
    guid="d36dc1fa-a38e-5aab-b6b8-c7ceca8f4744",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name",
    display_name="Togetic",
    searchable_by=["Togetic", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=84,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    family_id=175,
    abilities=[
        Attack(
            title="Shared Peace",
            game_text="Each player draws 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=shared_peace,
        ),
        Attack(
            title="Speed Dive",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
