"""Kangaskhan (SV3 165 -- JP SV3 090; English OBF/165). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def spike_draw(ctx):
    await ctx.deal_damage()
    await ctx.draw_cards(2)


card = PokemonCardDef(
    guid="316b5da6-841c-5a38-8af7-dfd453367ec5",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kangaskhan.Name",
    display_name="Kangaskhan",
    searchable_by=["Kangaskhan", "Basic"],
    subtypes=["Basic"],
    collector_number=165,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=115,
    abilities=[
        Attack(
            title="Headbutt",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Spike Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=spike_draw,
        ),
    ],
)
