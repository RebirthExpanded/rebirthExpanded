"""Flittle (SV1 101 -- JP SV1S 035; English SVI/101). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="6c992287-c706-5eee-9d7e-63ccb7acb84d",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name",
    display_name="Flittle",
    searchable_by=["Flittle", "Basic"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=955,
    abilities=[
        Attack(
            title="Spinning Attack",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
