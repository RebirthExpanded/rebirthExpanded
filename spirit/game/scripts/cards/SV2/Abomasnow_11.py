"""Abomasnow (SV2 11 -- JP SV2P 006; English PAF/101, PAL/11). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="aaf8a73e-5f05-5baf-b69d-e136d3002a9c",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Abomasnow.Name",
    display_name="Abomasnow",
    searchable_by=["Abomasnow", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name",
    family_id=459,
    abilities=[
        Ability(
            title="Freezing Disaster",
            game_text="Pokémon (both yours and your opponent's) can't be healed.",
            passive=pc.healing_block_passive(lambda target, carrier: True),
        ),
        Attack(
            title="Magnum Punch",
            game_text="",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)
