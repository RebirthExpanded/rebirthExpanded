"""Pancham (SV09 83 -- JP SV9 050; English JTG/83). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5a2a0ee0-7063-5cdc-b2f2-5872e18f921d",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name",
    display_name="Pancham",
    searchable_by=["Pancham", "Basic"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=674,
    abilities=[
        Attack(
            title="Corkscrew Punch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Focus Fist",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
