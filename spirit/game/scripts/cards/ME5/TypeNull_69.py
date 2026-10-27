"""Type: Null (ME5 69 -- JP M5 067; English PBL/69). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="128af4dd-7a5f-5035-af8f-6210ebe5e7dd",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name",
    display_name="Type: Null",
    searchable_by=["Type: Null", "Basic"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=772,
    abilities=[
        Attack(
            title="Power Edge",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
