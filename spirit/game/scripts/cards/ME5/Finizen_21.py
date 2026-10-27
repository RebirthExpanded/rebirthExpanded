"""Finizen (ME5 21 -- JP M5 020; English PBL/21). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="94b46dc3-73f7-57bc-8118-0a87dcb6e6f9",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name",
    display_name="Finizen",
    searchable_by=["Finizen", "Basic"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=963,
    abilities=[
        Attack(
            title="Draining Fin",
            game_text="Heal 20 damage from this Pokémon.",
            cost={PokemonTypes.WATER: 2},
            damage=20,
            effect=su.heal_attack(20),
        ),
    ],
)
