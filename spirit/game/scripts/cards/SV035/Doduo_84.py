"""Doduo (SV035 84 -- JP SV2a 084; English MEW/84, PAF/199). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="0d6fa103-a21a-528b-9761-26e3ee84314f",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name",
    display_name="Doduo",
    searchable_by=["Doduo", "Basic"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=84,
    abilities=[
        Attack(
            title="Reckless Charge",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.recoil_attack(10),
        ),
    ],
)
