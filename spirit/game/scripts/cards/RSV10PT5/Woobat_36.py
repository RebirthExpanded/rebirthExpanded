"""Woobat (RSV10PT5 36 -- JP SV11W 033; English WHT/119, WHT/36). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="160deaff-654f-58b3-9166-04c2b26be318",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name",
    display_name="Woobat",
    searchable_by=["Woobat", "Basic"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=527,
    abilities=[
        Attack(
            title="Heart Stamp",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
