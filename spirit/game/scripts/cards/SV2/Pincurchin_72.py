"""Pincurchin (SV2 72 -- JP SVC 006; English PAL/72). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="dedba794-f391-5900-b965-379f71314ca2",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pincurchin.Name",
    display_name="Pincurchin",
    searchable_by=["Pincurchin", "Basic"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=871,
    abilities=[
        Attack(
            title="Needle Crush",
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=70,
            effect=ac.discard_opponent_energy_attack(1),
        ),
    ],
)
