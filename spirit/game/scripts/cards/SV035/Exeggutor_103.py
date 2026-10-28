"""Exeggutor (SV035 103 -- JP SV2a 103; English MEW/103). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="9b986276-ba74-5a1b-a28f-b5f3141676c9",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggutor.Name",
    display_name="Exeggutor",
    searchable_by=["Exeggutor", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=103,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    abilities=[
        Attack(
            title="Psychic",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("defender"), 30, base=30),
        ),
        Attack(
            title="Hammer In",
            game_text="",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
