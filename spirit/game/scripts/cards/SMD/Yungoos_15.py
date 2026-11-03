"""Yungoos (SMD 15 -- JP SMD 015; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="e57d22e7-3cd8-5a8a-8389-7bfb244981b4",
    key="SMD",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yungoos.Name",
    display_name="Yungoos",
    searchable_by=["Yungoos", "Basic"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="SMD",
    regulation_mark="A",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=734,
    abilities=[
        Attack(
            title="Focused Fang",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
