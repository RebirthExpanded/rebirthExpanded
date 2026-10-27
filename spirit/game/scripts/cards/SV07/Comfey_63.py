"""Comfey (SV07 63 -- JP SV7 042; English SCR/63). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def flower_shower(ctx):
    await ctx.draw_cards(3)
    await ctx.draw_cards(3, player_id=ctx.opponent_id)


card = PokemonCardDef(
    guid="567ea745-e4ed-507b-afd8-bfca05b903cb",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Comfey.Name",
    display_name="Comfey",
    searchable_by=["Comfey", "Basic"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=764,
    abilities=[
        Attack(
            title="Flower Shower",
            game_text="Each player draws 3 cards.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=flower_shower,
        ),
        Attack(
            title="Play Rough",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator="+",
            effect=ac.flip_bonus(20),
        ),
    ],
)
