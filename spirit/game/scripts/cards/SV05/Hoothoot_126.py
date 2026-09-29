from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def silent_wing(ctx):
    """20. Your opponent reveals their hand."""
    await ctx.deal_damage()
    await ctx.reveal_hand(ctx.opponent_id)

card = PokemonCardDef(
    guid="1b66be2f-040b-5861-a68e-5a976721c135",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name",
    display_name="Hoothoot",
    searchable_by=["Hoothoot", "Basic", "Hoothoot"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=163,
    abilities=[
        Attack(
            title="Silent Wing",
            game_text="Your opponent reveals their hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=silent_wing,
        ),
    ],
)
