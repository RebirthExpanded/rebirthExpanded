"""Charmander (SVP 47 -- JP SVP 060; English SVP/47). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="f233104a-c0af-5856-98b7-a908a229772a",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    display_name="Charmander",
    searchable_by=["Charmander", "Basic"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=4,
    abilities=[
        Attack(
            title="Ember",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 2},
            damage=40,
            effect=ac.self_energy_discard_attack(1),
        ),
    ],
)
