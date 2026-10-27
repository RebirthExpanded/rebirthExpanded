"""Cetitan (SV08 54 -- JP SV7a 017; English SSP/201, SSP/54). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="1c6c4c2f-e4fe-54dc-aa73-eb6b5b63b89a",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cetitan.Name",
    display_name="Cetitan",
    searchable_by=["Cetitan", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name",
    family_id=974,
    abilities=[
        Ability(
            title="Solid Body",
            game_text="This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=pc.takes_less_passive(30),
        ),
        Attack(
            title="Dangerous Mouth",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=150,
        ),
    ],
)
