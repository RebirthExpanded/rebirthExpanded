"""Goomy (ME4 66 -- JP M4 064; English CRI/66). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="dec491cd-49a4-5ee4-85bf-bc441577945f",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Goomy.Name",
    display_name="Goomy",
    searchable_by=["Goomy", "Basic"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=704,
    abilities=[
        Attack(
            title="Absorb",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=su.heal_attack(30),
        ),
    ],
)
