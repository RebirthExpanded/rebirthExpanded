from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_item_card


async def proclaim_the_night(ctx):
    """The opponent can't play Item cards from hand during their next turn."""
    ctx.lock_plays(ctx.opponent_id, is_item_card)

card = PokemonCardDef(
    guid="8be72b91-6ce0-588b-9735-56f70d1682a5",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name",
    display_name="Hoothoot",
    searchable_by=["Hoothoot", "Basic", "Hoothoot"],
    subtypes=["Basic"],
    collector_number=119,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=163,
    abilities=[
        Attack(
            title="Proclaim the Night",
            game_text="Your opponent can't play any Item cards from his or her hand during his or her next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=0,
            effect=proclaim_the_night,
        ),
    ],
)
