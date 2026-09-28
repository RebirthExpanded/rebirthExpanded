from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def collect(ctx):
    """Draw a card."""
    await ctx.draw_cards(1)

card = PokemonCardDef(
    guid="004b5fdc-a90c-57b7-b1b8-bbc0d194f3fa",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    display_name="Electrike",
    searchable_by=["Electrike", "Basic", "Electrike"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=309,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=0,
            effect=collect,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
        ),
    ],
)
