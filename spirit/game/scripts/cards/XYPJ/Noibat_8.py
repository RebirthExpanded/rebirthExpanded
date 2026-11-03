"""Noibat (XYPJ 8 -- JP XYP 008; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="4f0e2520-38c3-5b5b-bffc-9e095345a949",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name",
    display_name="Noibat",
    searchable_by=["Noibat", "Basic"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=714,
    abilities=[
        Attack(
            title="Supersonic",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ac.condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
        Attack(
            title="Wing Attack",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)
