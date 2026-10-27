"""Nidoran ♀ (ME6A 73 -- JP M6a 073; English 30C/87). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="4619d204-5db0-5d70-94d9-83276341475e",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NidoranFemale.Name",
    display_name="Nidoran ♀",
    searchable_by=["Nidoran ♀", "Basic"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=29,
    abilities=[
        Attack(
            title="Growl",
            game_text="During your opponent's next turn, attacks used by the Defending Pokémon do 30 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pc.debuff_defender_attacks(30),
        ),
        Attack(
            title="Headbutt",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)
