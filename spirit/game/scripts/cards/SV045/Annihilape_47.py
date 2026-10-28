"""Annihilape (SV045 47 -- JP SV1V 051; English PAF/171, PAF/47, SVI/109). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="dddce97a-6d12-558d-9140-ecd3dee2e336",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Annihilape.Name",
    display_name="Annihilape",
    searchable_by=["Annihilape", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=47,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    family_id=56,
    abilities=[
        Attack(
            title="Rage Fist",
            game_text="This attack does 70 damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=70,
            damage_operator="x",
            effect=ac.damage_per(ac.count_prizes_taken("opponent"), 70),
        ),
        Attack(
            title="Dynamite Punch",
            game_text="This Pokémon also does 50 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=170,
            effect=ac.recoil_attack(50),
        ),
    ],
)
