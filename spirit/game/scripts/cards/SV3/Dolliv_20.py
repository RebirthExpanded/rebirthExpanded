"""Dolliv (SV3 20 -- JP SVD 010; English OBF/20). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="ebe69c2d-177b-5611-a81d-f6287fa26242",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dolliv.Name",
    display_name="Dolliv",
    searchable_by=["Dolliv", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Smoliv.Name",
    family_id=928,
    abilities=[
        Attack(
            title="Sunny Wind",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=su.heal_attack(30),
        ),
    ],
)
