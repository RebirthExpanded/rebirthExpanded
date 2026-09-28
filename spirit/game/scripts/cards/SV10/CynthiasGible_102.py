from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def rock_hurl(ctx):
    """20. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)

card = PokemonCardDef(
    guid="03a61c93-2f57-5a65-9dae-2a881e36afef",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGible.Name",
    display_name="Cynthia's Gible",
    searchable_by=["Cynthia's Gible", "Basic", "CynthiasGible"],
    subtypes=["Basic"],
    collector_number=102,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=443,
    abilities=[
        Attack(
            title="Rock Hurl",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=rock_hurl,
        ),
    ],
)
