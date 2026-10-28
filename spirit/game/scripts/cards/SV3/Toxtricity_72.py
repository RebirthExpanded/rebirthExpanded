"""Toxtricity (SV3 72 -- JP SV3 038; English OBF/72, PAF/141). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _bench_types(ctx) -> int:
    kinds = set()
    for p in ctx.my_bench():
        kinds.update(p.get_attribute(AttrID.POKEMON_TYPES) or [])
    return len(kinds)


card = PokemonCardDef(
    guid="33f8faa1-f51f-52b5-a5fd-500a7a82d20c",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricity.Name",
    display_name="Toxtricity",
    searchable_by=["Toxtricity", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    family_id=848,
    abilities=[
        Attack(
            title="Leer",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Loud Mix",
            game_text="This attack does 30 more damage for each different type of Pokémon on your Bench.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=ac.damage_per(_bench_types, 30, base=50),
        ),
    ],
)
