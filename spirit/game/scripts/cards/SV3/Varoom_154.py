"""Varoom (SV3 154 -- JP SV3 083; English OBF/154, OBF/206). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def spinning_draw(ctx):
    await ctx.deal_damage()
    await ctx.draw_cards(1)


card = PokemonCardDef(
    guid="27230cd2-85d7-58cc-b05a-0b54130e8f75",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name",
    display_name="Varoom",
    searchable_by=["Varoom", "Basic"],
    subtypes=["Basic"],
    collector_number=154,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=965,
    abilities=[
        Attack(
            title="Spinning Draw",
            game_text="Draw a card.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            effect=spinning_draw,
        ),
    ],
)
