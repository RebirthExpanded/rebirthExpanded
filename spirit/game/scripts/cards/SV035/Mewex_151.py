"""Mew ex (SV - 151 151/165 -- JP SV4a 076/190).

Basic Psychic Pokemon ex. HP 180, weakness Darkness x2, resistance
Fighting -30, retreat 0.

  Ability  Restart  Once during your turn, you may draw cards until you
                    have 3 cards in your hand.
  Genome Hacking  [CCC]  Choose 1 of your opponent's Active Pokemon's
                         attacks and use it as this attack.

Genome Hacking runs through the shared copy path (Copycat): the copied
attack's cost is not paid again, and a copied GX/VSTAR attack respects the
once-per-game rules.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import draw_until_effect
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef, def_for)


def _hand_below_three(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    deck = board.find_player_area(player_id, "deck")
    return len(hand.children if hand else []) < 3 and bool(deck and deck.children)


async def genome_hacking(ctx):
    target = ctx.opponent_active()
    if target is None:
        return
    attacks = [a for a in (getattr(def_for(target.archetype_id), "abilities", None) or [])
               if isinstance(a, Attack)]
    if not attacks:
        return
    options = [(target, a) for a in attacks]
    if len(options) == 1:
        chosen = options[0][1]
    else:
        picked = await ctx.choose_attack_to_copy(options, "Choose an attack to use")
        if picked is None:
            return
        chosen = picked[1]
    await ctx.use_attack(chosen)


card = PokemonCardDef(
    guid="4e1c90e9-fc10-54a5-a330-412144f23697",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewex.Name",
    display_name="Mew ex",
    searchable_by=["Mew ex", "Basic", "ex", "Mewex"],
    subtypes=["Basic", "ex"],
    collector_number=151,
    set_code="SV035",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=151,
    regulation_mark="G",
    abilities=[
        Ability(title="Restart",
                game_text="Once during your turn, you may draw cards until you have 3 cards in your hand.",
                activation=Activations.ONCE_PER_TURN, condition=_hand_below_three,
                effect=draw_until_effect(3)),
        Attack(title="Genome Hacking",
               game_text="Choose 1 of your opponent's Active Pokémon's attacks and use it as this attack.",
               cost={PokemonTypes.COLORLESS: 3}, damage=0, effect=genome_hacking),
    ],
)
