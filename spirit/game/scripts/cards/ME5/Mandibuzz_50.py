"""Mandibuzz (ME5 50 -- JP M5 048; English PBL/50). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_special_energy


def _has_special(pokemon) -> bool:
    return any(is_special_energy(e) for e in pokemon.children if e.__class__.__name__ == "EnergyEntity")


card = PokemonCardDef(
    guid="6d7699cf-cb19-5f52-86b6-363585a21381",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mandibuzz.Name",
    display_name="Mandibuzz",
    searchable_by=["Mandibuzz", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vullaby.Name",
    family_id=629,
    abilities=[
        Attack(
            title="Bone Sniper",
            game_text="This attack does 70 damage to 1 of your opponent's Pokémon that has any Special Energy attached. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 1},
            effect=ac.snipe_attack(70, pool=_has_special, prompt="Choose a Pokémon with Special Energy to take 70 damage"),
        ),
        Attack(
            title="Blasting Wind",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
