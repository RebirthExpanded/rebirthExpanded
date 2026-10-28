"""Cottonee (SV045 34 -- JP SVEM 007; English PAF/34). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="0007164f-a68e-5c34-9166-b68fa8801fe9",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    display_name="Cottonee",
    searchable_by=["Cottonee", "Basic"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=546,
    abilities=[
        Attack(
            title="Fickle Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
