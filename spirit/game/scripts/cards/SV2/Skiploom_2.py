"""Skiploom (SV2 2 -- JP SV2D 002; English PAF/97, PAL/2). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c9021148-a55b-5432-b16b-b28615d3d4a8",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name",
    display_name="Skiploom",
    searchable_by=["Skiploom", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name",
    family_id=187,
    abilities=[
        Ability(
            title="Drifting Dodge",
            game_text="If any damage is done to this Pokémon by attacks, flip a coin. If heads, prevent that damage.",
            passive=pc.flip_prevent_damage_passive("Drifting Dodge"),
        ),
        Attack(
            title="Flowery Zephyr",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=ac.snipe_attack(30, pool="bench", also_base=True),
        ),
    ],
)
