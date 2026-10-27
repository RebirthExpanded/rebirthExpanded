"""Greavard (ME1 65 -- JP M1S 047; English MEG/65). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="eb63050f-924d-5c5c-a8ff-d47cb460d0a3",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name",
    display_name="Greavard",
    searchable_by=["Greavard", "Basic"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=971,
    abilities=[
        Attack(
            title="Stampede",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title="Take Down",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=ac.recoil_attack(10),
        ),
    ],
)
