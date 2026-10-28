"""Tandemaus (SV045 73 -- JP SV2D 062; English PAF/209, PAF/73, PAL/166). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="05073693-b373-5b63-a4a2-96c018d665cc",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tandemaus.Name",
    display_name="Tandemaus",
    searchable_by=["Tandemaus", "Basic"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=924,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.draw_attack(2),
        ),
        Attack(
            title="Gentle Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)
