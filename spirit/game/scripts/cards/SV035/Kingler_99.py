"""Kingler (SV035 99 -- JP SV2a 099; English MEW/99). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="d4dc3fa1-e75c-52b7-b4da-8d45ff50a7b8",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingler.Name",
    display_name="Kingler",
    searchable_by=["Kingler", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=99,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krabby.Name",
    family_id=98,
    abilities=[
        Attack(
            title="Hammer Arm",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.WATER: 3},
            damage=90,
            effect=ac.mill_attack(1),
        ),
        Attack(
            title="Guillotine",
            game_text="",
            cost={PokemonTypes.WATER: 4},
            damage=220,
        ),
    ],
)
