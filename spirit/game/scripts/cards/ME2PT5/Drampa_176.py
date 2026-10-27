"""Drampa (ME2PT5 176 -- JP MC 621; English ASC/176). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="6017f99d-7650-5918-9048-3c8075d7d20a",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drampa.Name",
    display_name="Drampa",
    searchable_by=["Drampa", "Basic"],
    subtypes=["Basic"],
    collector_number=176,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=780,
    abilities=[
        Attack(
            title="Gentle Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Dragon Strike",
            game_text="During your next turn, this Pokémon can't use Dragon Strike.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            locks_next_turn=True,
        ),
    ],
)
