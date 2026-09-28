from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def hold_still(ctx):
    """Heal 10 damage from this Pokemon."""
    await ctx.heal(10, ctx.attacker)

card = PokemonCardDef(
    guid="8993f087-d5cc-5fd6-aae0-9eac0a6642c6",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LilliesCutiefly.Name",
    display_name="Lillie's Cutiefly",
    searchable_by=["Lillie's Cutiefly", "Basic", "LilliesCutiefly"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    family_id=742,
    abilities=[
        Attack(
            title="Hold Still",
            game_text="Heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=0,
            effect=hold_still,
        ),
    ],
)
