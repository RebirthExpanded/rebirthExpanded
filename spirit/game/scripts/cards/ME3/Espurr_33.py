"""Espurr (ME3 33 -- JP M3 032; English POR/33, POR/95). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="07e99eab-49ad-5702-a3da-bb4d61657f7f",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name",
    display_name="Espurr",
    searchable_by=["Espurr", "Basic"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=677,
    abilities=[
        Attack(
            title="Nap",
            game_text="Heal 20 damage from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.heal_attack(20),
        ),
        Attack(
            title="Stampede",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
