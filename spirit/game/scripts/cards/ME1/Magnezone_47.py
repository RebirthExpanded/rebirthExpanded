"""Magnezone (ME1 47 -- JP M1S 029; English MEG/47). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _evolved_this_turn(ctx) -> bool:
    state = ctx.session.turn_state
    return state.entered_play_turn.get(ctx.attacker.entity_id) == state.turn_number


card = PokemonCardDef(
    guid="c5b9ec54-a727-5998-a593-5cb43c72571e",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name",
    display_name="Magnezone",
    searchable_by=["Magnezone", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=47,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    family_id=81,
    abilities=[
        Attack(
            title="Upper Spark",
            game_text="If this Pokémon evolved from Magneton during this turn, this attack does 120 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=50,
            damage_operator="+",
            effect=ac.bonus_if(_evolved_this_turn, 120),
        ),
        Attack(
            title="Flashing Bolt",
            game_text="During your next turn, this Pokémon can't use Flashing Bolt.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=160,
            locks_next_turn=True,
        ),
    ],
)
