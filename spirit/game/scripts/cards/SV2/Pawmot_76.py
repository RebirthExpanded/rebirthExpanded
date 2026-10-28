"""Pawmot (SV2 76 -- JP SVC 009; English PAL/76). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="b79eafdd-72dd-5bcf-ac26-4b8a4717ea67",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmot.Name",
    display_name="Pawmot",
    searchable_by=["Pawmot", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=76,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmo.Name",
    family_id=921,
    abilities=[
        Attack(
            title="Mach Bolt",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=40,
        ),
        Attack(
            title="Electric Fist",
            game_text="This attack also does 60 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=100,
            effect=ac.snipe_attack(60, pool="bench", also_base=True),
        ),
    ],
)
