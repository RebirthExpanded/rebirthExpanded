"""Arven's Toedscool (SV10 109 -- JP SV9a 047; English DRI/109). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="2a8d9586-478d-56f4-abce-4f8c81dad46f",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensToedscool.Name",
    display_name="Arven's Toedscool",
    searchable_by=["Arven's Toedscool", "Basic"],
    subtypes=["Basic"],
    collector_number=109,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=948,
    abilities=[
        Attack(
            title="Slight Intrusion",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.recoil_attack(10),
        ),
    ],
)
