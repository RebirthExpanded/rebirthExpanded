"""Iron Boulder (SV085 46 -- JP SV7 047; English PRE/46, SCR/71). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _same_hands(ctx) -> bool:
    return len(ctx.hand()) == len(ctx.hand(ctx.opponent_id))


card = PokemonCardDef(
    guid="a4e0c1a4-1993-522e-bc70-340259c3bbc5",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronBoulder.Name",
    display_name="Iron Boulder",
    searchable_by=["Iron Boulder", "Basic", "Future"],
    subtypes=["Basic", "Future"],
    collector_number=46,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=0,
    abilities=[
        Attack(
            title="Adjusted Horn",
            game_text="If you don't have the same number of cards in your hand as your opponent, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=ac.bonus_if(_same_hands, 0, else_nothing=True),
        ),
    ],
)
