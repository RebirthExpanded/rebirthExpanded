"""Koraidon (ME5 47 -- JP M5 045; English PBL/47). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_evolution_pokemon


def _evolved_defender(ctx) -> bool:
    return ctx.defender is not None and is_evolution_pokemon(ctx.defender)


card = PokemonCardDef(
    guid="7a771915-353b-5ed2-8059-0c42edce0c45",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koraidon.Name",
    display_name="Koraidon",
    searchable_by=["Koraidon", "Basic"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=1007,
    abilities=[
        Attack(
            title="Battle Claw",
            game_text="If your opponent's Active Pokémon is an Evolution Pokémon, this attack does 30 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_evolved_defender, 30),
        ),
        Attack(
            title="Gaia Impact",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=ac.self_energy_discard_attack(all_energy=True),
        ),
    ],
)
