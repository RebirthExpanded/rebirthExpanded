"""Salandit (SV07 23 -- JP SV7 013; English ASC/34, SCR/23). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="00a167c5-ea02-5675-82b6-4c4ac2407ac5",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name",
    display_name="Salandit",
    searchable_by=["Salandit", "Basic"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=757,
    abilities=[
        Attack(
            title="Ember",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
