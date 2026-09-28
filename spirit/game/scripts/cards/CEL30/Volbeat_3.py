from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import _gust


async def luring_glow(ctx):
    """Switch in 1 of the opponent's Benched Pokemon to the Active Spot."""
    if ctx.opponent_bench():
        await _gust(ctx)

card = PokemonCardDef(
    guid="8968d82b-340e-5993-9b87-623e0dfd76ba",
    key="CEL30",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volbeat.Name",
    display_name="Volbeat",
    searchable_by=["Volbeat", "Basic", "Volbeat"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="CEL30",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=313,
    abilities=[
        Attack(
            title="Luring Glow",
            game_text="Switch in 1 of your opponent's Benched Pok\u00e9mon to the Active Spot.",
            cost={PokemonTypes.GRASS: 1},
            damage=0,
            effect=luring_glow,
        ),
        Attack(
            title="Bug Buzz",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)
