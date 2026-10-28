"""Miltank (SV4 147 -- JP SV4M 053; English PAR/147). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _healed_this_turn(ctx) -> bool:
    return ctx.attacker.entity_id in ctx.session.turn_state.healed_entities


card = PokemonCardDef(
    guid="f08fa81c-a366-5d16-825e-ac574413f052",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miltank.Name",
    display_name="Miltank",
    searchable_by=["Miltank", "Basic"],
    subtypes=["Basic"],
    collector_number=147,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=241,
    abilities=[
        Attack(
            title="Lively Tackle",
            game_text="If this Pokémon was healed during this turn, this attack does 90 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=ac.bonus_if(_healed_this_turn, 90),
        ),
    ],
)
