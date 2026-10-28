"""Seviper (SV1 128 -- JP SV1S 053; English SVI/128). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="a387a96a-9e92-5389-b680-25c7ec80203a",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seviper.Name",
    display_name="Seviper",
    searchable_by=["Seviper", "Basic"],
    subtypes=["Basic"],
    collector_number=128,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=336,
    abilities=[
        Attack(
            title="Spit Poison",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Venoshock",
            game_text="If your opponent's Active Pokémon is Poisoned, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=ac.bonus_if(ac.defender_has_condition(SpecialConditions.POISONED), 120),
        ),
    ],
)
