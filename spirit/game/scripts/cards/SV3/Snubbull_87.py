"""Snubbull (SV3 87 -- JP SVD 049; English OBF/87). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="2547a70f-7aea-5d2f-a8e8-d6179faac013",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snubbull.Name",
    display_name="Snubbull",
    searchable_by=["Snubbull", "Basic"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=209,
    abilities=[
        Attack(
            title="Gnaw",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.recoil_attack(10),
        ),
    ],
)
