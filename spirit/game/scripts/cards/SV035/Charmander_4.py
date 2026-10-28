"""Charmander (SV035 4 -- JP SV2a 004; English MEW/168, MEW/4, PAF/109, PAF/7). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def blazing_destruction(ctx):
    if ctx.stadium_in_play() is not None:
        await ctx.discard_stadium()


card = PokemonCardDef(
    guid="57b09545-9db6-5e0e-b19d-d6c24ea3baad",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    display_name="Charmander",
    searchable_by=["Charmander", "Basic"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=4,
    abilities=[
        Attack(
            title="Blazing Destruction",
            game_text="Discard a Stadium in play.",
            cost={PokemonTypes.FIRE: 1},
            effect=blazing_destruction,
        ),
        Attack(
            title="Steady Firebreathing",
            game_text="",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
        ),
    ],
)
