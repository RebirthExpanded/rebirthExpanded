"""Swalot (SV07 92 -- JP SV7 062; English SCR/92). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


def _more_energy(ctx) -> bool:
    return ac.count_energy("self", cards=True)(ctx) > ac.count_energy("defender", cards=True)(ctx)


card = PokemonCardDef(
    guid="b59fe935-362d-5e7b-acda-1249da3952d8",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swalot.Name",
    display_name="Swalot",
    searchable_by=["Swalot", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=92,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gulpin.Name",
    family_id=316,
    abilities=[
        Attack(
            title="Devouring Mouth",
            game_text="If this Pokémon has more Energy attached than your opponent's Active Pokémon, this attack does 160 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            damage_operator="+",
            effect=ac.bonus_if(_more_energy, 160),
        ),
        Attack(
            title="Venomous Hit",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
