"""Skwovet (SV3 178 -- JP SVD 099; English OBF/178). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c82e2c6e-fd2f-54e1-bc8a-4402cb19fbfa",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skwovet.Name",
    display_name="Skwovet",
    searchable_by=["Skwovet", "Basic"],
    subtypes=["Basic"],
    collector_number=178,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=819,
    abilities=[
        Attack(
            title="Nicked Nibble",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ac.mill_attack(1),
        ),
        Attack(
            title="Gentle Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
