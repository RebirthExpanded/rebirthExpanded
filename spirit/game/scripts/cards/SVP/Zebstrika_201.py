"""Zebstrika (SVP 201 -- JP SVP 212; English SVP/201). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def full_speed(ctx):
    hand = list(ctx.hand())
    if hand:
        await ctx.discard_cards(hand)
    await ctx.draw_cards(6)


card = PokemonCardDef(
    guid="53c1f02b-1f05-5082-8c0e-9b4c38a958c0",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zebstrika.Name",
    display_name="Zebstrika",
    searchable_by=["Zebstrika", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=201,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name",
    family_id=522,
    abilities=[
        Attack(
            title="Full Speed",
            game_text="Discard your hand and draw 6 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=full_speed,
        ),
        Attack(
            title="Head Bolt",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
