"""Whismur (SM - Celestial Storm 116/168 -- JP SM10b 071/? "Sky Legend").

Basic Colorless Pokemon. HP 60, weakness Fighting x2, retreat 2.

  Bawl   [C]     You can use this attack only if you go second, and only
                 on your first turn. Your opponent can't play any Trainer
                 cards from their hand during their next turn.
  Pound  [CC] 20
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_trainer_card


def _second_players_first_turn(board, player_id, pokemon=None) -> bool:
    ts = getattr(board, "turn_state", None)
    return ts is not None and ts.turn_number == 2


async def bawl(ctx):
    ctx.lock_plays(ctx.opponent_id, is_trainer_card)


card = PokemonCardDef(
    guid="2cd24b7d-1ad2-53df-baf4-072211341098",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whismur.Name",
    display_name="Whismur",
    searchable_by=["Whismur", "Basic"],
    subtypes=["Basic"],
    collector_number=116,
    set_code="SM7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=293,
    abilities=[
        Attack(title="Bawl",
               game_text="You can use this attack only if you go second, and only on your first turn. Your opponent can't play any Trainer cards from their hand during their next turn.",
               cost={PokemonTypes.COLORLESS: 1}, damage=0,
               condition=_second_players_first_turn, usable_first_turn=True,
               effect=bawl),
        Attack(title="Pound", game_text="", cost={PokemonTypes.COLORLESS: 2}, damage=20),
    ],
)
