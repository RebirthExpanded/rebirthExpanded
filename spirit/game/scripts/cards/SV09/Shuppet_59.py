"""Shuppet (SV09 59 -- JP SV9 035; English ASC/90, JTG/59). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="dcd6a78d-ba34-5077-a82a-9b4582562581",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    display_name="Shuppet",
    searchable_by=["Shuppet", "Basic"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=353,
    abilities=[
        Attack(
            title="Spooky Shot",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)
