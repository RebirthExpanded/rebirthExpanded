"""Bronzor (ME5 63 -- JP M5 061; English PBL/63). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _metal_defender(ctx) -> bool:
    d = ctx.defender
    from spirit.game.session.effects import live_pokemon_types
    return d is not None and PokemonTypes.METAL.value in live_pokemon_types(d)


card = PokemonCardDef(
    guid="fe1f5e9e-127d-5e21-87fc-f7be07117817",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    display_name="Bronzor",
    searchable_by=["Bronzor", "Basic"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=436,
    abilities=[
        Attack(
            title="Mirror Attack",
            game_text="If your opponent's Active Pokémon is a Metal Pokémon, this attack does 30 more damage.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            damage_operator="+",
            effect=ac.bonus_if(_metal_defender, 30),
        ),
    ],
)
