"""Yveltal (SV4 118 -- JP SV3a 039; English PAR/118, PAR/205). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_evolution_pokemon


def _evolved_defender(ctx) -> bool:
    return ctx.defender is not None and is_evolution_pokemon(ctx.defender)


card = PokemonCardDef(
    guid="125d3e9f-938e-5433-8516-c1ed55ba3cb2",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yveltal.Name",
    display_name="Yveltal",
    searchable_by=["Yveltal", "Basic"],
    subtypes=["Basic"],
    collector_number=118,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=717,
    abilities=[
        Attack(
            title="Cross-Cut",
            game_text="If your opponent's Active Pokémon is an Evolution Pokémon, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_evolved_defender, 60),
        ),
        Attack(
            title="Dark Edge",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
