"""Glimmet (SV06 108 -- JP SV6 062; English TWM/108). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="f1493494-19d1-530d-8603-2cc858ab4db3",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmet.Name",
    display_name="Glimmet",
    searchable_by=["Glimmet", "Basic"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=969,
    abilities=[
        Attack(
            title="Rock Shot",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
