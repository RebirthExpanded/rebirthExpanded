"""Gastrodon (SV08 107 -- JP SV8 066; English SSP/107). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc

from spirit.game.session.effects import is_stage2_pokemon


def _sticky(pokemon, carrier) -> bool:
    return (carrier._containing_area_name() == "bench" and pokemon._containing_area_name() == "bench"
            and is_stage2_pokemon(pokemon))


card = PokemonCardDef(
    guid="e3482f6e-c3db-5923-a2cf-a9c568b92ba0",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gastrodon.Name",
    display_name="Gastrodon",
    searchable_by=["Gastrodon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=107,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shellos.Name",
    family_id=422,
    abilities=[
        Ability(
            title="Sticky Bind",
            game_text="As long as this Pokémon is on your Bench, Benched Stage 2 Pokémon (both yours and your opponent's) have no Abilities.",
            passive=pc.ability_lock_passive(_sticky),
        ),
        Attack(
            title="Mud Shot",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
