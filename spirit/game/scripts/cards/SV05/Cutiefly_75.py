from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def mini_drain(ctx):
    """10. Heal 10 damage from this Pokemon."""
    await ctx.deal_damage()
    await ctx.heal(10, ctx.attacker)

card = PokemonCardDef(
    guid="17bb79a9-d6cb-547d-a227-6988ceedd792",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cutiefly.Name",
    display_name="Cutiefly",
    searchable_by=["Cutiefly", "Basic", "Cutiefly"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=742,
    abilities=[
        Attack(
            title="Mini Drain",
            game_text="Heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=mini_drain,
        ),
    ],
)
