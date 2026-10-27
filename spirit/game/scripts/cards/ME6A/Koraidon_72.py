"""Koraidon (ME6A 72 -- JP M6a 072; English 30C/86). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c12440c3-455c-5f46-9d9f-36f53c75a3a1",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koraidon.Name",
    display_name="Koraidon",
    searchable_by=["Koraidon", "Basic"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=1007,
    abilities=[
        Attack(
            title="Low Kick",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
        ),
        Attack(
            title="Collision Course",
            game_text="Discard 2 Fighting Energy from this Pokémon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
            effect=ac.self_energy_discard_attack(count=2, energy_type=PokemonTypes.FIGHTING),
        ),
    ],
)
