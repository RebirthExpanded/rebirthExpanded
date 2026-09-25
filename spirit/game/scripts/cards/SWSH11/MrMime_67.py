from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import apply_protection
from spirit.game.card_effects.support_common import rock_paper_scissors


async def tricky_slap(ctx):
    """Play Rock-Paper-Scissors until someone wins; if the attacker wins,
    shield this Pokemon from all damage/effects next turn."""
    await ctx.deal_damage()
    if await rock_paper_scissors(ctx):
        await apply_protection(ctx, prevent=True, effects_too=True)


card = PokemonCardDef(
    guid="21585a85-4646-52f6-9140-311efd26202e",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic", "MrMime"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=122,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Tricky Slap",
            game_text="You and your opponent play Rock-Paper-Scissors until someone wins. If you win, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=tricky_slap,
        ),
    ],
)
