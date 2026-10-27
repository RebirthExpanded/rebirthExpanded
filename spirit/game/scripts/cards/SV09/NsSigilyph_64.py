"""N's Sigilyph (SV09 64 -- JP SV9 040; English JTG/64). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def victory_symbol(ctx):
    if ac.count_prizes_remaining("mine")(ctx) == 1:
        await ctx.win_game("Victory Symbol")


card = PokemonCardDef(
    guid="8848f728-25a6-52f4-bea4-b23c1096d85c",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsSigilyph.Name",
    display_name="N's Sigilyph",
    searchable_by=["N's Sigilyph", "Basic"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=561,
    abilities=[
        Attack(
            title="Psychic Sphere",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
        Attack(
            title="Victory Symbol",
            game_text="If you use this attack when you have exactly 1 Prize card remaining, you win this game.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=victory_symbol,
        ),
    ],
)
