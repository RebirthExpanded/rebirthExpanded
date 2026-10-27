"""Totodile (ME2PT5 41 -- JP MC 165; English ASC/41). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="1a7b1a91-e425-5ee1-9c65-ac83a091127a",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name",
    display_name="Totodile",
    searchable_by=["Totodile", "Basic"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=158,
    abilities=[
        Attack(
            title="Slight Intrusion",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.WATER: 2},
            damage=40,
            effect=ac.recoil_attack(10),
        ),
    ],
)
