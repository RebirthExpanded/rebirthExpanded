"""Rowlet (SMPJ 290 -- JP SMP 290; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import SpecialConditions


card = PokemonCardDef(
    guid="51fea93a-607a-564e-a127-5ebf2f4d7a9a",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rowlet.Name",
    display_name="Rowlet",
    searchable_by=["Rowlet", "Basic"],
    subtypes=["Basic"],
    collector_number=290,
    set_code="SMPJ",
    regulation_mark="B",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=722,
    abilities=[
        Attack(
            title="Scream",
            game_text="Both Active Pokémon are now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ac.condition_attack(SpecialConditions.CONFUSED, both_actives=True),
        ),
    ],
)
