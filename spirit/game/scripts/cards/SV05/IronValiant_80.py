"""Iron Valiant (SV05 80 -- JP SV5M 035; English TEF/80). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import TrainerType
from spirit.game.data_utils import subtypes_for as _subs


def _supporter_with_sub_played(ctx, sub) -> bool:
    return any(ttype == TrainerType.SUPPORTER.value and sub in (_subs(aid) or [])
               for aid, _name, ttype in ctx.session.turn_state.trainers_played)


async def calculation(ctx):
    await ctx.reorder_deck_top(4)


def _future_supporter(ctx) -> bool:
    return _supporter_with_sub_played(ctx, "Future")


card = PokemonCardDef(
    guid="82a87863-b25a-54fc-b1b7-03bb389d8143",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronValiant.Name",
    display_name="Iron Valiant",
    searchable_by=["Iron Valiant", "Basic", "Future"],
    subtypes=["Basic", "Future"],
    collector_number=80,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=1006,
    abilities=[
        Attack(
            title="Calculation",
            game_text="Look at the top 4 cards of your deck and put them back in any order.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=calculation,
        ),
        Attack(
            title="Majestic Sword",
            game_text="If you played a Future Supporter card from your hand during this turn, this attack does 100 more damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=ac.bonus_if(_future_supporter, 100),
        ),
    ],
)
