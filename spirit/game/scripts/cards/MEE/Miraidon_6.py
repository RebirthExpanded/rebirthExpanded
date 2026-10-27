"""Miraidon (MEE 6 -- JP MEE 006; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="4e89585d-982c-57b8-9803-be10616f0093",
    key="MEE",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miraidon.Name",
    display_name="Miraidon",
    searchable_by=["Miraidon", "Basic"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="MEE",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1008,
    abilities=[
        Attack(
            title="Slash",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Flash Bolt",
            game_text="During your next turn, this Pokémon can't use Flash Bolt.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            locks_next_turn=True,
        ),
    ],
)
