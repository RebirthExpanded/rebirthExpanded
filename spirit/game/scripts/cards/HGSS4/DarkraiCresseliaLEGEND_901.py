"""Darkrai & Cresselia LEGEND -- the combined Pokemon (HS - Triumphant
99/102 + 100/102 -- JP 30th CELEBRATION M6a 151/152, the art on the two
halves).

Darkness / Psychic LEGEND. HP 150, weakness Fighting x2 and Psychic x2,
no resistance, retreat 2. When Knocked Out, the opponent takes 2 Prizes.

  Lost Crisis   [DDCC] 100  Put 2 Energy attached to Darkrai & Cresselia
                            LEGEND in the Lost Zone. If the Defending
                            Pokemon is Knocked Out by damage from this
                            attack, put that Pokemon and all cards attached
                            to it in the Lost Zone instead of discarding
                            them.
  Moon's Invite [P]         Move as many damage counters on your opponent's
                            Pokemon as you like to any of your opponent's
                            other Pokemon in any way you like.

Runtime-only: the two halves (DarkraiCresseliaLEGEND_99 / _100) name it;
played together from hand they become this Pokemon (session/legends.py).
Lost Crisis pays its 2 Energy as provided units (a Double Colorless is
both) and routes a Knock Out by its damage through ctx.knockout_destinations,
which sends the whole stack to the Lost Zone. Number 901 is this pool's
own for the combined face; the halves carry the set numbers.
"""

import json

from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, LegendPokemonDef
from spirit.game.session.passives import energy_provided_options

NAME = "com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiCresseliaLEGEND.Name"


def _units(board, energy) -> int:
    options = energy_provided_options(board, energy)
    return max((len(o) for o in options), default=1)


async def lost_crisis(ctx):
    await ctx.deal_damage()
    # 2 Energy (provided units) from this Pokemon to the Lost Zone.
    need = 2
    while need > 0:
        pool = ctx.attached_energies(ctx.attacker)
        if not pool:
            break
        picks = [pool[0]] if len(pool) == 1 else await ctx.choose_cards(
            pool, 1, minimum=1, prompt="Choose an Energy to put in the Lost Zone.")
        if not picks:
            break
        need -= _units(ctx.board, picks[0])
        await ctx.move_to_lost_zone(picks)
    defender = ctx.defender
    if defender is not None and defender in ctx.knockouts \
            and defender.entity_id in ctx.attack_damage:
        ctx.knockout_destinations[defender.entity_id] = ("lostZone", True)


async def moons_invite(ctx):
    opp = ctx.opponent_pokemon_in_play()
    await ctx.move_damage_counters_freely(opp, opp)


LOST_CRISIS = Attack(
    title="Lost Crisis",
    game_text="Put 2 Energy attached to Darkrai & Cresselia LEGEND in the Lost Zone. If the Defending Pokémon is Knocked Out by damage from this attack, put that Pokémon and all cards attached to it in the Lost Zone instead of discarding them.",
    cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
    damage=100,
    effect=lost_crisis,
)
MOONS_INVITE = Attack(
    title="Moon's Invite",
    game_text="Move as many damage counters on your opponent's Pokémon as you like to any of your opponent's other Pokémon in any way you like.",
    cost={PokemonTypes.PSYCHIC: 1},
    effect=moons_invite,
)


card = LegendPokemonDef(
    prize_count=2,
    guid="295debd7-a1fa-5150-a5cc-7a8195f97a8d",
    key="HGSS4",
    name=NAME,
    display_name="Darkrai & Cresselia LEGEND",
    searchable_by=["Darkrai & Cresselia LEGEND", "LEGEND", "DarkraiCresseliaLEGEND"],
    subtypes=["LEGEND"],
    collector_number=901,
    set_code="HGSS4",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DARKNESS, PokemonTypes.PSYCHIC],
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=491,
    abilities=[LOST_CRISIS, MOONS_INVITE],
)
# Two Weaknesses (Fighting and Psychic, x2 each): the list the damage
# calculation reads.
card.extra_attributes[str(AttrID.WEAKNESS_TYPES.value)] = {
    "type": "json",
    "value": json.dumps([PokemonTypes.FIGHTING.value, PokemonTypes.PSYCHIC.value]),
}
