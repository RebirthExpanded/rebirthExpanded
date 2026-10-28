"""Golisopod (SV4 49 -- JP SV3a 010; English PAR/49). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="4d786459-731a-5d61-827d-e0f06da3805b",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golisopod.Name",
    display_name="Golisopod",
    searchable_by=["Golisopod", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    family_id=767,
    abilities=[
        Attack(
            title="Powerful Cross",
            game_text="This attack does 20 damage for each card in your opponent's hand.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            damage_operator="x",
            effect=ac.damage_per(ac.count_hand("opponent"), 20),
        ),
        Attack(
            title="Waterfall",
            game_text="",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
