"""Salvatore (SV - Temporal Forces 160/162 -- JP SV5M 067/071).

Supporter.

  "Search your deck for a card that has no Abilities and evolves from 1 of
   your Pokemon, and put it onto that Pokemon to evolve it. Then, shuffle
   your deck. You can use this card on a Pokemon you put down when you
   were setting up to play or on a Pokemon that was put into play this
   turn."

Wally with one more filter: the evolution card must print no Ability.
That is the CARD's own text -- Wobbuffet BREAK prints only an attack, so
Salvatore can put it onto a Wobbuffet, even though the BREAK then retains
Bide Barricade from the card underneath. Playable only with a Pokemon in
play that has such an evolution in the pool at all (has_evolution's
reading, narrowed the same way), so in a format where Wobbuffet's only
evolution is the Expanded-only BREAK, a Standard Wobbuffet is no target.

Like Wally it skips the evolution turn gates: a Pokemon played this turn,
or put down at setup, may be evolved.
"""

from spirit.game.attributes import AttrID, Rarities
from spirit.game.card_effects.pokemon import has_printed_ability
from spirit.game.card_effects.support_common import evolves_from, pokemon_can_still_evolve
from spirit.game.data_utils import Ability, Attack, SupporterCardDef


def _prints_no_ability(definition) -> bool:
    abilities = getattr(definition, "abilities", None) or []
    return not any(isinstance(a, Ability) and not isinstance(a, Attack)
                   for a in abilities)


def _salvatore_targets(board, player_id):
    """Pokemon with an Ability-less evolution that can still come out of the
    deck (not every copy of it in the discard pile)."""
    return [p for p in board.pokemon_in_play(player_id)
            if pokemon_can_still_evolve(board, player_id, p, _prints_no_ability)]


def _salvatore_condition(board, player_id):
    return bool(_salvatore_targets(board, player_id))


async def salvatore(ctx):
    """Evolve one of your Pokemon with an Ability-less evolution card."""
    candidates = _salvatore_targets(ctx.board, ctx.player_id)
    if not candidates:
        return
    target = await ctx.choose_pokemon(candidates, "Choose a Pokémon to evolve")
    if target is None:
        return
    logic_name = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    if not logic_name:
        return
    picks = await ctx.search_deck(
        lambda c, name=logic_name: (
            evolves_from(c, name)
            and not has_printed_ability(c)),
        count=1, minimum=0,
        prompt="Choose a card with no Abilities that evolves from that Pokémon.",
    )
    if picks:
        await ctx.evolve_pokemon(target, picks[0])
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="06ea1cb3-b6c8-575d-aca6-ebd222962b26",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Salvatore.Name",
    display_name="Salvatore",
    searchable_by=["Salvatore", "Supporter"],
    subtypes=["Supporter"],
    collector_number=160,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=salvatore,
    condition=_salvatore_condition,
)
