from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import TrainerType
from spirit.game.data_utils import subtypes_for


def _ancient_supporter_played(ctx) -> bool:
    return any(ttype == TrainerType.SUPPORTER.value and "Ancient" in subtypes_for(aid)
               for aid, _name, ttype in ctx.session.turn_state.trainers_played)


async def land_collapse(ctx):
    """Mill 1 of the opponent's deck, 4 after an Ancient Supporter this turn."""
    count = 4 if _ancient_supporter_played(ctx) else 1
    await ctx.discard_cards(ctx.deck_top(count, player_id=ctx.opponent_id))

card = PokemonCardDef(
    guid="8356cb34-2900-580a-8134-4b4a0d778379",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreatTusk.Name",
    display_name="Great Tusk",
    searchable_by=["Great Tusk", "Basic", "Ancient", "GreatTusk"],
    subtypes=["Basic", "Ancient"],
    collector_number=97,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=984,
    abilities=[
        Attack(
            title="Land Collapse",
            game_text="Discard the top card of your opponent's deck. If you played an Ancient Supporter card from your hand during this turn, discard 3 more cards in this way.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=0,
            effect=land_collapse,
        ),
        Attack(
            title="Giant Tusk",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=160,
        ),
    ],
)
