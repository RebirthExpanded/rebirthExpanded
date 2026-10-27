"""Spritzee (ME3 35 -- JP M3 034; English POR/35). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="49eb02da-1be2-554e-b1cb-67cbe8c8824a",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spritzee.Name",
    display_name="Spritzee",
    searchable_by=["Spritzee", "Basic"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=682,
    abilities=[
        Attack(
            title="Sweet Scent",
            game_text="Heal 30 damage from 1 of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.heal_targets(30, "choice"),
        ),
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
