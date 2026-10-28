"""Cloyster (SV035 91 -- JP SV2a 091; English MEW/91). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="ee4853fd-7bb2-500a-95d4-a8f1d8a4ab27",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cloyster.Name",
    display_name="Cloyster",
    searchable_by=["Cloyster", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=91,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shellder.Name",
    family_id=90,
    abilities=[
        Attack(
            title="Protect Charge",
            game_text="During your opponent's next turn, this Pokémon takes 80 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 2},
            damage=80,
            effect=pc.protect_next_turn(reduce=80),
        ),
    ],
)
