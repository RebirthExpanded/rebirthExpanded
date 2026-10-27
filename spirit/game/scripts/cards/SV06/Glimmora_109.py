"""Glimmora (SV06 109 -- JP SV6 063; English TWM/109). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="efa522c7-df7f-55f3-a819-a38b60b5deef",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmora.Name",
    display_name="Glimmora",
    searchable_by=["Glimmora", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=109,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmet.Name",
    family_id=969,
    abilities=[
        Attack(
            title="Stun Poison",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ac.condition_attack(SpecialConditions.PARALYZED, SpecialConditions.POISONED, flip=True),
        ),
        Attack(
            title="Venoshock",
            game_text="If your opponent's Active Pokémon is Poisoned, this attack does 100 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(ac.defender_has_condition(SpecialConditions.POISONED), 100),
        ),
    ],
)
