"""Bronzor (SV3 144 -- JP SV2P 050; English OBF/144). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def mirror_draw(ctx):
    n = len(ctx.hand(ctx.opponent_id)) - len(ctx.hand())
    if n > 0:
        await ctx.draw_cards(n)


card = PokemonCardDef(
    guid="9b9720c5-b45f-5810-b29e-8bcd0a1bd440",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    display_name="Bronzor",
    searchable_by=["Bronzor", "Basic"],
    subtypes=["Basic"],
    collector_number=144,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=436,
    abilities=[
        Attack(
            title="Mirror Draw",
            game_text="Draw cards until you have the same number of cards in your hand as your opponent.",
            cost={PokemonTypes.METAL: 1},
            effect=mirror_draw,
        ),
        Attack(
            title="Speed Dive",
            game_text="",
            cost={PokemonTypes.METAL: 2},
            damage=30,
        ),
    ],
)
