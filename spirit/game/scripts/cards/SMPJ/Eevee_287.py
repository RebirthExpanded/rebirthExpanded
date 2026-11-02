"""Eevee (SMPJ 287 -- JP SMP 287; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import SpecialConditions


card = PokemonCardDef(
    guid="ec84da45-2bbd-5fc2-9f2c-d4277b88ad1b",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic"],
    subtypes=["Basic"],
    collector_number=287,
    set_code="SMPJ",
    regulation_mark="B",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Scream",
            game_text="Both Active Pokémon are now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ac.condition_attack(SpecialConditions.CONFUSED, both_actives=True),
        ),
    ],
)
