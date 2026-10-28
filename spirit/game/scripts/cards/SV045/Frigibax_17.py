"""Frigibax (SV045 17 -- JP SV4a 051; English PAF/128, PAF/17). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="8ead9336-a57b-50a9-a77c-938870b0e12e",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Frigibax.Name",
    display_name="Frigibax",
    searchable_by=["Frigibax", "Basic"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=996,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={PokemonTypes.WATER: 1},
            effect=su.draw_attack(1),
        ),
        Attack(
            title="Beat",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
