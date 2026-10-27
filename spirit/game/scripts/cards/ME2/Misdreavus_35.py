"""Misdreavus (ME2 35 -- JP M2 035; English PFL/35). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="1855118c-9a6f-5285-9cb2-7b1bb324fda9",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name",
    display_name="Misdreavus",
    searchable_by=["Misdreavus", "Basic"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=200,
    abilities=[
        Attack(
            title="Petty Grudge",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)
