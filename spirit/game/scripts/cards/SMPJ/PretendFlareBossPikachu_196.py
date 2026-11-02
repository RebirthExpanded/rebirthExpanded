"""Pretend Flare Boss Pikachu (SMPJ 196 -- JP SMP 196; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _beautiful_world(ctx):
    """Printed damage, then discard the Stadium in play."""
    await ctx.deal_damage()
    if ctx.stadium_in_play() is not None:
        await ctx.discard_stadium()


card = PokemonCardDef(
    guid="2c1b1902-ae5e-577f-8d3a-dacc325d11eb",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PretendFlareBossPikachu.Name",
    display_name="Pretend Flare Boss Pikachu",
    searchable_by=["Pretend Flare Boss Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=196,
    set_code="SMPJ",
    regulation_mark="B",
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
            title="Beautiful World?",
            game_text="Discard any Stadium card in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=_beautiful_world,
        ),
        Attack(
            title="Pika Punch",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
