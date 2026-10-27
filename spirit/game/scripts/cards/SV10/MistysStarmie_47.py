"""Misty's Starmie (SV10 47 -- JP SV9a 024; English DRI/47). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _evolved_this_turn(ctx) -> bool:
    state = ctx.session.turn_state
    return state.entered_play_turn.get(ctx.attacker.entity_id) == state.turn_number


card = PokemonCardDef(
    guid="00c22bd1-9110-5669-a5c4-3f9c260a166e",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysStarmie.Name",
    display_name="Misty's Starmie",
    searchable_by=["Misty's Starmie", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MistysStaryu.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Abrupt Flash",
            game_text="If this Pokémon evolved from Misty's Staryu during this turn, this attack does 80 more damage.",
            cost={PokemonTypes.WATER: 1},
            damage=60,
            damage_operator="+",
            effect=ac.bonus_if(_evolved_this_turn, 80),
        ),
    ],
)
