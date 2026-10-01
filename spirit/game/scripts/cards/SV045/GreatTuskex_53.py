from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import Triggers
from spirit.game.card_effects.pokemon import in_active_spot


def _quaking_applies(ctx) -> bool:
    return in_active_spot(ctx.board, ctx.player_id, ctx.source) and bool(ctx.deck())


async def quaking_demolition(ctx):
    """End of my turn, in the Active Spot: discard the top 5 of my deck
    (mandatory)."""
    if not _quaking_applies(ctx):
        return
    await ctx.discard_cards(ctx.deck_top(5))


async def great_bash(ctx):
    """260, not affected by effects on the opponent's Active Pokemon."""
    await ctx.deal_damage(ignore_target_effects=True)

card = PokemonCardDef(
    guid="d9454711-a7b6-5719-8297-38a202fc9b37",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreatTuskex.Name",
    display_name="Great Tusk ex",
    searchable_by=["Great Tusk ex", "Basic", "ex", "Ancient", "GreatTuskex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=53,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=984,
    abilities=[
        Ability(
            title="Quaking Demolition",
            game_text="Once at the end of your turn (after your attack), if this Pok\u00e9mon is in the Active Spot, you must discard the top 5 cards of your deck.",
            trigger=Triggers.END_OF_TURN,
            effect=quaking_demolition,
            trigger_applies=_quaking_applies,
        ),
        Attack(
            title="Great Bash",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=260,
            effect=great_bash,
        ),
    ],
)
