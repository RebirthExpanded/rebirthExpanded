"""Hitmontop (ME2PT5 102 -- JP MC 367; English ASC/102, ASC/240). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="5a5633ab-552c-583a-92e0-fe78b8ddeab1",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmontop.Name",
    display_name="Hitmontop",
    searchable_by=["Hitmontop", "Basic"],
    subtypes=["Basic"],
    collector_number=102,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=236,
    abilities=[
        Attack(
            title="Spin and Draw",
            game_text="Shuffle your hand into your deck. Then, draw 6 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.shuffle_hand_into_deck_draw(6),
        ),
        Attack(
            title="Low Kick",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
