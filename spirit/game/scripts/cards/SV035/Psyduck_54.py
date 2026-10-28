"""Psyduck (SV035 54 -- JP SV2a 054; English MEW/175, MEW/54). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon



class _Overthink(Passive):
    """Game-level: during that turn the victim's coins all land tails."""

    def __init__(self, victim, turn):
        self.victim, self.turn = victim, turn

    def forces_coin_tails(self, flipper_id, carrier):
        board = getattr(carrier, "board", None)
        return flipper_id == self.victim and self._active(carrier)

    def _active(self, carrier):
        from spirit.game.models.board import board_of
        board = board_of(carrier)
        ts = getattr(board, "turn_state", None) if board is not None else None
        return ts is not None and ts.turn_number == self.turn


async def overthink(ctx):
    ctx.add_game_passive(_Overthink(ctx.opponent_id, ctx.session.turn_state.turn_number + 1))


card = PokemonCardDef(
    guid="a5ee3809-3986-57ea-a16b-38eedf344e1b",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    display_name="Psyduck",
    searchable_by=["Psyduck", "Basic"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=54,
    abilities=[
        Attack(
            title="Overthink",
            game_text="During your opponent's next turn, whenever they flip a coin, treat it as tails.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=overthink,
        ),
        Attack(
            title="Water Gun",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
