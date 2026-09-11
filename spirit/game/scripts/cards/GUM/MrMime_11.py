"""Mr. Mime (SM - Detective Pikachu 11/18 -- JP SMP2 007/024).

Basic Psychic Pokemon. HP 80, weakness Psychic x2, retreat 1.

  Ability  Pantomime  When you play this Pokemon from your hand onto your
                      Bench during your turn, you may switch 1 of your
                      face-down Prize cards with the top card of your deck.
  PC Juggling  [P] 20x  Flip 4 coins. This attack does 20 damage for each
                        heads.

The switch is blind on both sides: the Prize picked is not looked at, and
the deck card that replaces it goes down unseen.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.trainers import has_face_down_prize
from spirit.game.data_utils import (Ability, Attack, PokemonCardDef,
                                    Triggers)


def _pantomime_condition(board, player_id, pokemon=None) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return has_face_down_prize(board, player_id) and bool(deck and deck.children)


async def pantomime(ctx):
    if not await ctx.ask_yes_no(
            "Switch 1 of your face-down Prize cards with the top card of your deck?"):
        return
    await ctx.swap_prize_with_deck_top()


card = PokemonCardDef(
    guid="7451884c-8397-50ab-9ba5-ec559b0ad4d8",
    key="GUM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="GUM",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=122,
    abilities=[
        Ability(
            title="Pantomime",
            game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may switch 1 of your face-down Prize cards with the top card of your deck.",
            trigger=Triggers.ON_PLAY,
            condition=_pantomime_condition,
            effect=pantomime,
        ),
        Attack(
            title="PC Juggling",
            game_text="Flip 4 coins. This attack does 20 damage for each heads.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=flip_damage(coins=4, per_heads=20),
        ),
    ],
)
