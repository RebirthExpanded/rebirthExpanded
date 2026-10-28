"""Jumpluff (SV2 3 -- JP SV2D 003; English PAF/98, PAL/3). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c37b558b-03cf-50a5-8186-df4adbbdf3e9",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jumpluff.Name",
    display_name="Jumpluff",
    searchable_by=["Jumpluff", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name",
    family_id=187,
    abilities=[
        Ability(
            title="Drifting Dodge",
            game_text="If any damage is done to this Pokémon by attacks, flip a coin. If heads, prevent that damage.",
            passive=pc.flip_prevent_damage_passive("Drifting Dodge"),
        ),
        Attack(
            title="Fluffy Breeze",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            effect=ac.snipe_attack(30, pool="bench", also_base=True),
        ),
    ],
)
