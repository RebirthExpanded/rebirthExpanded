"""Prinplup (ME2 28 -- JP M2 028; English PFL/28). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c8f1af17-c76c-5ffb-b612-afe1b2574cda",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    display_name="Prinplup",
    searchable_by=["Prinplup", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Piplup.Name",
    family_id=393,
    abilities=[
        Attack(
            title="Peck",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Targeted Dive",
            game_text="This attack does 70 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=ac.snipe_attack(70, pool="bench"),
        ),
    ],
)
