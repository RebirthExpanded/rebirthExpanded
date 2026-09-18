"""Klefki (XY - Steam Siege 80/114 -- JP XY11-Bb 040/054, the art here).

Basic Fairy Pokemon. HP 70, weakness Metal x2, resistance Darkness -20,
retreat 1.

  Wonder Lock  (Ability)  Once during your turn (before your attack), if
                          this Pokemon is on your Bench, you may discard all
                          cards attached to it and attach it to 1 of your
                          Pokemon as a Pokemon Tool. The Pokemon this card
                          is attached to takes no damage from attacks from
                          your opponent's Mega Evolution Pokemon. Discard
                          this card at the end of your opponent's turn.
  Fairy Wind   [YC]  30

The Pokemon card ITSELF becomes the Tool (ctx.attach_as_tool): it leaves
the Bench with its damage and effects cleared, its attachments go to the
discard pile first, and while attached it wears a Tool's TRAINER_TYPE --
so Garbotoxin sees a Tool on Garbodor, Field Blower / Xerosic's
Machinations can discard it, Jamming Tower switches its text off, and it
is no Pokemon in play (Eternal Zone keeps working around it). The rest of
the card follows from that:

- The "no damage from Mega Evolution Pokemon" clause is the card's own
  passive, live only while it is a Tool and only for its holder. Mega
  Evolution Pokemon are the XY "MEGA" cards; the SV Mega Evolution ex
  are not covered (ruling).
- "Discard this card at the end of your opponent's turn" is the Tool's
  text, so Jamming Tower (Tools have no effect) keeps it on the Pokemon,
  while an Ability lock does not stop the discard (it is no Ability) --
  it only stops Wonder Lock from being used at all.
- Back in the discard pile it is a Klefki card again (Rescue Carrier can
  return it).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.data_utils import (
    Ability, Activations, Attack, PokemonCardDef, subtypes_for,
)
from spirit.game.session.passives import tool_slots_free


def _is_mega(pokemon) -> bool:
    # The XY-era Mega Evolution Pokemon ("M ...-EX") only: the SV Mega
    # Evolution ex are not "Mega Evolution Pokemon" to this text (ruling).
    return "MEGA" in subtypes_for(pokemon.archetype_id)


def _wonder_lock_shield(calc, carrier) -> bool:
    """Only as a Tool, only for the Pokemon it rides, only versus Megas."""
    if not getattr(carrier, "acts_as_tool", False):
        return False
    holder = getattr(carrier, "parent", None)
    return (calc.target is holder and calc.attacker is not None
            and _is_mega(calc.attacker))


def _on_bench_with_a_holder(board, player_id, pokemon) -> bool:
    bench = board.find_player_area(player_id, "bench")
    if bench is None or pokemon.parent is not bench:
        return False
    return any(p is not pokemon and tool_slots_free(board, p) > 0
               for p in board.pokemon_in_play(player_id))


async def wonder_lock(ctx):
    klefki = ctx.source
    candidates = [p for p in ctx.my_pokemon_in_play()
                  if p is not klefki and tool_slots_free(ctx.board, p) > 0]
    if not candidates:
        return
    holder = await ctx.choose_pokemon(
        candidates, "Choose a Pokémon to attach Klefki to as a Pokémon Tool")
    if holder is None:
        return
    attached = list(klefki.children)
    if attached:
        await ctx.discard_cards(attached)
    if await ctx.attach_as_tool(klefki, holder):
        klefki.discard_at_opponents_turn_end = True


card = PokemonCardDef(
    guid="074e0671-eb1c-512e-b13b-ad33fc266aae",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klefki.Name",
    display_name="Klefki",
    searchable_by=["Klefki", "Basic"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=707,
    passive=prevent_damage_when(_wonder_lock_shield),
    abilities=[
        Ability(
            title="Wonder Lock",
            game_text="Once during your turn (before your attack), if this Pokémon is on your Bench, you may discard all cards attached to it and attach it to 1 of your Pokémon as a Pokémon Tool. The Pokémon this card is attached to takes no damage from attacks from your opponent's Mega Evolution Pokémon. Discard this card at the end of your opponent's turn.",
            activation=Activations.ONCE_PER_TURN,
            condition=_on_bench_with_a_holder,
            effect=wonder_lock,
        ),
        Attack(
            title="Fairy Wind",
            game_text="",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
