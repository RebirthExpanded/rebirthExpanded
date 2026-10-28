"""Smoliv (SV3 19 -- JP SVD 009; English OBF/19). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="8e340227-d6ae-594d-9cba-e76310209826",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smoliv.Name",
    display_name="Smoliv",
    searchable_by=["Smoliv", "Basic"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=928,
    abilities=[
        Attack(
            title="Absorb",
            game_text="Heal 10 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=su.heal_attack(10),
        ),
    ],
)
