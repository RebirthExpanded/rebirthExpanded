"""Mega Camerupt ex (ME1 22 -- JP M1L 013; English MEG/156, MEG/22). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5e2333b4-0f34-5a86-8371-77678ba6913d",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaCameruptex.Name",
    display_name="Mega Camerupt ex",
    searchable_by=["Mega Camerupt ex", "Stage 1", "ex", "SV_Mega"],
    subtypes=["Stage 1", "ex", "SV_Mega"],
    collector_number=22,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name",
    family_id=322,
    abilities=[
        Attack(
            title="Roasting Heat",
            game_text="If your opponent's Active Pokémon is Burned, this attack does 160 more damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(ac.defender_has_condition(SpecialConditions.BURNED), 160),
        ),
        Attack(
            title="Volcanic Meteor",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=280,
            effect=ac.self_energy_discard_attack(count=2),
        ),
    ],
)
