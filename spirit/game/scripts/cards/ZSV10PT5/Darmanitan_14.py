"""Darmanitan (ZSV10PT5 14 -- JP SV11B 014; English BLK/14, BLK/98). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="12d52a0a-2d4b-519f-aff6-31f9ef041e26",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darmanitan.Name",
    display_name="Darmanitan",
    searchable_by=["Darmanitan", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name",
    family_id=554,
    abilities=[
        Attack(
            title="Searing Flame",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=ac.condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Smashing Headbutt",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=ac.self_energy_discard_attack(count=2),
        ),
    ],
)
