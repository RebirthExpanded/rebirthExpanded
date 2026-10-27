"""Miltank (SV085 81 -- JP SVM 096; English PRE/81). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

def _used_last_turn(title):
    def cond(ctx) -> bool:
        history = ctx.board.turn_state.attacks_prev_turn_by_player.get(ctx.player_id) or []
        return any(used_id == ctx.attacker.entity_id and t == title for used_id, _arch, t in history)
    return cond


def _rolled_last_turn(board, player_id, pokemon=None) -> bool:
    ts = getattr(board, "turn_state", None)
    history = ts.attacks_prev_turn_by_player.get(player_id) or [] if ts is not None else []
    return pokemon is not None and any(used_id == pokemon.entity_id and t == "Rollout" for used_id, _a, t in history)


card = PokemonCardDef(
    guid="5e35a8a8-c1ba-5872-b0bd-63b4478ed851",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miltank.Name",
    display_name="Miltank",
    searchable_by=["Miltank", "Basic"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=241,
    abilities=[
        Attack(
            title="Rollout",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Moomoo Rolling",
            game_text="You can use this attack only if this Pokémon used Rollout during your last turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=100,
            condition=_rolled_last_turn,
        ),
    ],
)
