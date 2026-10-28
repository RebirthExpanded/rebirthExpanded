"""Shuppet (SV1 87 -- JP SV1V 040; English SVI/87). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_item_card


async def enveloping_shadow(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Enveloping Shadow")
    if results and results[0]:
        ctx.lock_plays(ctx.opponent_id, is_item_card)


card = PokemonCardDef(
    guid="2846b0e8-be45-5dc1-8ca0-64689e45508d",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    display_name="Shuppet",
    searchable_by=["Shuppet", "Basic"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=353,
    abilities=[
        Attack(
            title="Enveloping Shadow",
            game_text="Flip a coin. If heads, during your opponent's next turn, they can't play any Item cards from their hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=enveloping_shadow,
        ),
    ],
)
