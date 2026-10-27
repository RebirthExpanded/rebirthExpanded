"""Darumaka (ME2 15 -- JP M2 015; English PFL/15). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import PokemonTypes as _PT


card = PokemonCardDef(
    guid="6aa2c3f7-785b-57c6-b583-cf1c014b26c5",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name",
    display_name="Darumaka",
    searchable_by=["Darumaka", "Basic"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=554,
    abilities=[
        Attack(
            title="Blaze Ball",
            game_text="This attack does 20 more damage for each Fire Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("self", _PT.FIRE), 20, base=10),
        ),
    ],
)
