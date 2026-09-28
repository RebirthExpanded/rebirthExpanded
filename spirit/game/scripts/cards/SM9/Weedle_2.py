from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import _gust


async def tangle_drag(ctx):
    """Switch 1 of the opponent's Benched Pokemon with their Active."""
    if ctx.opponent_bench():
        await _gust(ctx)

card = PokemonCardDef(
    guid="50ccfdc3-297a-5872-82ee-f356d6d1f26d",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name",
    display_name="Weedle",
    searchable_by=["Weedle", "Basic", "Weedle"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="SM9",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=13,
    abilities=[
        Attack(
            title="Tangle Drag",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=0,
            effect=tangle_drag,
        ),
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
