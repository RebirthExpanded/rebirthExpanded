"""Sudowoodo (XY - BREAKpoint 67/122 -- JP XY9 048/080).

Basic Fighting. HP 90, weakness Water x2, retreat 2.

  Watch and Learn  [FC]  If your opponent's Pokemon used an attack during
                         their last turn, use it as this attack.

The one copy attack in the family that takes no choice from the board: it
replays what THEY did, so the source is the turn ledger rather than a
Pokemon in play. attacks_used_last_turn records (entity, archetype, title)
per declared attack, and the archetype is what makes this work after the
attacker is gone -- a Pokemon that attacked and was then Knocked Out still
lends its attack here.

Whose turn it was matters: attacks_used_last_turn is simply "last turn",
so the entries are filtered against the titles the OPPONENT declared on
their own previous turn. An extra turn (Dialga-GX) does not confuse it,
because both ledgers rotate together.

Two attacks in one turn is rare but possible (Festival Lead), so with more
than one candidate the player picks; with exactly one there is nothing to
ask. The copy goes through the shared path, which keeps the re-entry guard
and the once-per-game GX/VSTAR checks.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef, def_for


def _their_last_turn_attacks(ctx):
    """(display Pokemon, Attack) for every attack they declared last turn."""
    state = ctx.session.turn_state
    titles = set(state.attack_titles_prev_turn_by_player.get(ctx.opponent_id) or [])
    if not titles:
        return []
    board = ctx.board
    fallback = board.active_pokemon(ctx.opponent_id)
    pairs = []
    seen = set()
    for entity_id, archetype_id, title in state.attacks_used_last_turn:
        if title not in titles:
            continue
        definition = def_for(archetype_id)
        for ability in getattr(definition, "abilities", None) or []:
            if not isinstance(ability, Attack) or ability.title != title:
                continue
            if (archetype_id, title) in seen:
                break
            seen.add((archetype_id, title))
            # The Pokemon that used it may be gone; the panel needs something
            # to draw, so their Active stands in for it.
            user = board.get_entity(entity_id) or fallback
            pairs.append((user, ability))
            break
    return pairs


async def watch_and_learn(ctx):
    """Use the attack they used last turn as this attack."""
    candidates = _their_last_turn_attacks(ctx)
    if not candidates:
        return
    if len(candidates) == 1:
        _, chosen = candidates[0]
    else:
        picked = await ctx.choose_attack_to_copy(
            candidates, "Choose an attack to copy")
        if picked is None:
            return
        _, chosen = picked
    await ctx.use_attack(chosen)


card = PokemonCardDef(
    guid="7073c86c-eb5f-56ca-9809-328e390b5794",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name",
    display_name="Sudowoodo",
    searchable_by=["Sudowoodo", "Basic", "Sudowoodo"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=185,
    abilities=[
        Attack(
            title="Watch and Learn",
            game_text="If your opponent's Pokémon used an attack during their last turn, use it as this attack.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            effect=watch_and_learn,
        ),
    ],
)
