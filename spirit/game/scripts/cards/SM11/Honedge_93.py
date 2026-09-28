from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def slashing_cutter(ctx):
    """10, not affected by Weakness or Resistance."""
    await ctx.deal_damage(ignore_weakness=True, ignore_resistance=True)

card = PokemonCardDef(
    guid="09ddc029-f790-57f3-b8b1-17457bbded26",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name",
    display_name="Honedge",
    searchable_by=["Honedge", "Basic", "Honedge"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=679,
    abilities=[
        Attack(
            title="Slashing Cutter",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=slashing_cutter,
        ),
    ],
)
