"""Charcadet (SV1 39 -- JP SV1S 010; English SVI/39). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="7e4cf052-10e9-558e-9ec3-f137e4ac8f04",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    display_name="Charcadet",
    searchable_by=["Charcadet", "Basic"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=935,
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
