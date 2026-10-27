"""Ralts (ME1 58 -- JP M1S 040; English ASC/87, MEG/58). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="93460e14-a7e4-5004-b3d1-c286069f7938",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name",
    display_name="Ralts",
    searchable_by=["Ralts", "Basic"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=280,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.draw_attack(1),
        ),
        Attack(
            title="Headbutt",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
