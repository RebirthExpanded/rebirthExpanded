"""Tandemaus (SV1 159 -- JP SV1V 064; English SVI/159). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="a32e9d43-6330-545d-bd36-46c0456ccc5b",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tandemaus.Name",
    display_name="Tandemaus",
    searchable_by=["Tandemaus", "Basic"],
    subtypes=["Basic"],
    collector_number=159,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=924,
    abilities=[
        Attack(
            title="Gnaw",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
