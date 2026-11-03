"""Team Rocket's Mareep (SV10 72 -- JP SV10 034; English DRI/72). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.session.effects import is_item_card


card = PokemonCardDef(
    guid="9e18d728-4eaf-5650-84ee-a47913d15f2f",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMareep.Name",
    display_name="Team Rocket's Mareep",
    searchable_by=["Team Rocket's Mareep", "Basic"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=179,
    abilities=[
        Attack(
            title="Procurement",
            game_text="Search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(is_item_card, count=1, reveal=True, prompt="Choose an Item card."),
        ),
        Attack(
            title="Tiny Bolt",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)
