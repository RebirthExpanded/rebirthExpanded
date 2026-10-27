"""Zubat (ME4 49 -- JP M4 048; English CRI/49). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="ad232eb2-5fa5-56a3-8744-bc9600e17428",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name",
    display_name="Zubat",
    searchable_by=["Zubat", "Basic"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=41,
    abilities=[
        Attack(
            title="Supersonic",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
