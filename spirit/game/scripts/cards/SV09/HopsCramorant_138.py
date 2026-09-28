from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_prizes_remaining


async def fickle_spitting(ctx):
    """120, only while the opponent has exactly 3 or 4 Prize cards left."""
    if count_prizes_remaining("opponent")(ctx) in (3, 4):
        await ctx.deal_damage()

card = PokemonCardDef(
    guid="688a1b12-10e5-5cf8-af1f-fc3913343683",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsCramorant.Name",
    display_name="Hop's Cramorant",
    searchable_by=["Hop's Cramorant", "Basic", "HopsCramorant"],
    subtypes=["Basic"],
    collector_number=138,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=845,
    abilities=[
        Attack(
            title="Fickle Spitting",
            game_text="If your opponent doesn't have exactly 3 or 4 Prize cards remaining, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=fickle_spitting,
        ),
    ],
)
