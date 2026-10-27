"""Gimmighoul (ME1 67 -- JP M1L 019; English MEG/67). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="76ba351b-0773-5d40-97ed-a8f679a77dfb",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gimmighoul.Name",
    display_name="Gimmighoul",
    searchable_by=["Gimmighoul", "Basic"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=999,
    abilities=[
        Attack(
            title="Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
