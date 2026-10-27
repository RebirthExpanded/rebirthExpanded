"""Scraggy (ME2PT5 134 -- JP M2a 109; English ASC/134). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def knock_off(ctx):
    await ctx.deal_damage()
    await ac.discard_random_from_hand(ctx, ctx.opponent_id, count=1)


card = PokemonCardDef(
    guid="4c5290c6-ac3d-5774-8874-d3ab11adec2d",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    display_name="Scraggy",
    searchable_by=["Scraggy", "Basic"],
    subtypes=["Basic"],
    collector_number=134,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=559,
    abilities=[
        Attack(
            title="Knock Off",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=knock_off,
        ),
    ],
)
