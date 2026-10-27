"""Escavalier (ZSV10PT5 60 -- JP SV11B 065; English BLK/138, BLK/60). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="e0ca01e6-8e1c-5824-a199-744f8862744a",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Escavalier.Name",
    display_name="Escavalier",
    searchable_by=["Escavalier", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name",
    family_id=588,
    abilities=[
        Attack(
            title="Wild Lance",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.METAL: 1},
            damage=90,
            effect=ac.recoil_attack(30),
        ),
    ],
)
