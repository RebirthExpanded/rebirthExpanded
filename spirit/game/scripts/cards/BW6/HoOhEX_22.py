"""Ho-Oh-EX (BW - Dragons Exalted 22/124 -- JP BW5 026/050, the art here).

Basic Fire Pokemon-EX. HP 160, weakness Water x2, resistance Fighting -20,
retreat 2.

  Ability  Rebirth   Once during your turn (before your attack), if this
                     Pokemon is in your discard pile, you may flip a coin.
                     If heads, put this Pokemon onto your Bench and attach
                     3 different types of basic Energy cards from your
                     discard pile to this Pokemon.
  Rainbow Burn [CCC] 20+  Does 20 more damage for each different type of
                     basic Energy attached to this Pokemon.

Rebirth is an out-of-zone Ability usable from the discard pile, the way
Prehistoric Call and Propagation are; once per turn per copy (Q&A: two
Ho-Oh-EX in the discard are two uses). It needs a free Bench slot to be
offered at all, and -- Eternal Zone -- a Bench it may be put onto: Ho-Oh
is Fire, so under a working Eternal Zone the Ability is not offered, and
were it reached anyway the put is refused.

The Energy (Q&A): one of each different basic type, as many as the
discard holds up to 3 -- two types is two cards, and with three or more
types the full 3 must be attached (no stopping at 2). Cards of one type
are interchangeable, so only the CHOICE of types is asked, and only when
more than three are on offer. Heads with no basic Energy at all still
benches the bird.

The order on the Japanese print is "attach, then put onto the Bench"; the
English one benches first. The put is done first here because an Energy
attaches to a Pokemon in play; the result is the same board.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Activations
from spirit.game.session.effects import is_basic_energy
from spirit.game.session.passives import bench_space, putting_into_play_blocked


def _basic_energy_types(cards):
    """Ordered distinct basic-Energy types among `cards`."""
    seen = []
    for card in cards:
        if not is_basic_energy(card):
            continue
        for t in card.get_attribute(AttrID.POKEMON_TYPES) or []:
            if t not in seen:
                seen.append(t)
    return seen


def _rebirth_condition(board, player_id, card) -> bool:
    if bench_space(board, player_id) <= 0:
        return False
    # Eternal Zone: a Fire Pokemon may not be put onto that Bench.
    return not putting_into_play_blocked(board, player_id, card)


async def rebirth(ctx):
    """Heads: onto the Bench, with one basic Energy of each of up to 3
    different types from the discard pile."""
    heads = await ctx.flip_coins(1, title="Rebirth")
    if not heads or not heads[0]:
        return
    if not await ctx.bench_pokemon(ctx.source):
        return
    discard = list(ctx.discard_pile())
    by_type = {}
    for card in discard:
        if not is_basic_energy(card):
            continue
        for t in card.get_attribute(AttrID.POKEMON_TYPES) or []:
            by_type.setdefault(t, card)
    representatives = list(by_type.values())
    if len(representatives) > 3:
        representatives = await ctx.choose_cards(
            representatives, 3, minimum=3,
            prompt="Choose 3 different types of basic Energy to attach.",
        )
    for energy in representatives[:3]:
        await ctx.attach_energy(energy, ctx.source)


async def rainbow_burn(ctx):
    """20, plus 20 per different type of basic Energy attached."""
    types = _basic_energy_types(ctx.board.attached_energies(ctx.attacker))
    await ctx.deal_damage(20 + 20 * len(types))


card = PokemonCardDef(
    guid="1281c5b0-f8f8-590c-a9c3-cf730df271e2",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOhEX.Name",
    display_name="Ho-Oh-EX",
    searchable_by=["Ho-Oh-EX", "Basic", "EX", "HoOhEX"],
    subtypes=["Basic", "EX"],
    collector_number=22,
    set_code="BW6",
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=250,
    abilities=[
        Ability(
            title="Rebirth",
            game_text="Once during your turn (before your attack), if this Pokémon is in your discard pile, you may flip a coin. If heads, put this Pokémon onto your Bench and attach 3 different types of basic Energy cards from your discard pile to this Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            usable_from="discard",
            condition=_rebirth_condition,
            effect=rebirth,
        ),
        Attack(
            title="Rainbow Burn",
            game_text="Does 20 more damage for each different type of basic Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            effect=rainbow_burn,
        ),
    ],
)
