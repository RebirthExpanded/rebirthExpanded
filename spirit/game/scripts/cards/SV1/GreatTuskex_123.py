"""Great Tusk ex (SV1 123 -- JP SV1S 049; English SVI/123, SVI/230, SVI/246). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def bedrock_breaker(ctx):
    await ctx.deal_damage()
    if ctx.stadium_in_play() is not None:
        await ctx.discard_stadium()


card = PokemonCardDef(
    guid="d994bec3-596a-5b19-a2a0-fde9092c169b",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreatTuskex.Name",
    display_name="Great Tusk ex",
    searchable_by=["Great Tusk ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=123,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=984,
    abilities=[
        Attack(
            title="Bedrock Breaker",
            game_text="Discard a Stadium in play.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            effect=bedrock_breaker,
        ),
        Attack(
            title="Gigantic Tusks",
            game_text="This Pokémon also does 50 damage to itself.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=250,
            effect=ac.recoil_attack(50),
        ),
    ],
)
