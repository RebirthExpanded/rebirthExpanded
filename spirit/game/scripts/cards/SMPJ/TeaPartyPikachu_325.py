"""Tea Party Pikachu (SMPJ 325 -- JP SMP 325; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _petal_gathering(ctx):
    """Each player draws 2 cards."""
    await ctx.draw_cards(2)
    await ctx.draw_cards(2, ctx.opponent_id)


card = PokemonCardDef(
    guid="9c099eb5-d368-54ad-9319-5e030afdc641",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeaPartyPikachu.Name",
    display_name="Tea Party Pikachu",
    searchable_by=["Tea Party Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=325,
    set_code="SMPJ",
    regulation_mark="C",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Petal Gathering",
            game_text="Each player draws 2 cards.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_petal_gathering,
        ),
        Attack(
            title="Electro Ball",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
