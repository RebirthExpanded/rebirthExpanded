"""Toxel (SV4 69 -- JP SV4M 026; English PAR/69). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5a0e5b73-85f0-5f4e-aa93-367f44372eb2",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    display_name="Toxel",
    searchable_by=["Toxel", "Basic"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=848,
    abilities=[
        Attack(
            title="Whimsy Tackle",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=60,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
