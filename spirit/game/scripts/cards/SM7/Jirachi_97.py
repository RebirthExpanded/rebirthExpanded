"""Jirachi {*} (SM - Celestial Storm 97/168).

Basic Metal Pokemon, Prism Star. HP 80, weakness Fire x2, resistance
Psychic -20, retreat 1.

  Wish Upon a Star       Ability. If you took this Pokemon as a face-down
                         Prize card during your turn and your Bench isn't
                         full, before you put it into your hand, you may
                         put it onto your Bench and take 1 more Prize card.
  Perish Dream   [CCC] 10  This Pokemon is now Asleep. At the end of your
                         opponent's next turn, the Defending Pokemon will
                         be Knocked Out.

Wish Upon a Star rides ON_TAKEN_AS_PRIZE, the window Dream Ball already
opens. Three things follow from the wording, and each one is a real gate:

FACE-DOWN. A Prize turned over by Town Map was not taken face down, so it
opens no window at all. _take_prizes now remembers which picks were face
down before move_card clears the flag -- Dream Ball reads the same way
("you took it as a face-down Prize card"), so both cards get this.

TAKEN AS A PRIZE. The window belongs to the prize-take path, so it does
not open for the cards that merely put a Prize into your hand -- Hisuian
Heavy Ball and Gladion go through look_at_prizes_take, which never touches
it. Peonia does take Prize cards and so does open it.

NOT AN IN-PLAY ABILITY. Garbotoxin and Silent Lab reach Pokemon in play,
in hand and in the discard pile; neither names the Prize cards, so neither
switches this off. This is why "before you put it into your hand" is taken
literally -- _take_prizes opens the window while the card is still a Prize.
Fired one step later, from hand, Garbotoxin WOULD silence it.

"Your Bench isn't full" is the Bench you actually have, so a Stadium that
shrinks it fills it sooner; the check goes through
effective_bench_capacity rather than the raw constant.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import delayed_knockout
from spirit.game.session.passives import effective_bench_capacity


async def wish_upon_a_star(ctx):
    """Taken face down as a Prize: you may Bench it and take 1 more Prize."""
    bench = ctx.board.find_player_area(ctx.player_id, "bench")
    # "your Bench isn't full" means the Bench you actually have: a Stadium
    # that shrinks it (Collapsed Stadium, Parallel City) fills it sooner.
    if bench is None or len(bench.children) >= effective_bench_capacity(
            ctx.board, ctx.player_id):
        return
    if not await ctx.ask_yes_no(
            "Put this Pokémon onto your Bench and take 1 more Prize card?"):
        return
    if not await ctx.bench_pokemon(ctx.source):
        return
    await ctx.take_prizes(1)


async def perish_dream(ctx):
    """10, this Pokemon falls Asleep, and the Defending Pokemon is Knocked
    Out at the end of the opponent's next turn."""
    await ctx.deal_damage()
    from spirit.game.attributes import SpecialConditions
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)
    await delayed_knockout(ctx)


card = PokemonCardDef(
    guid="729d4c52-67e8-5cbd-95ee-521f14c8505b",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.JirachiPrismStar.Name",
    display_name="Jirachi {*}",
    searchable_by=["Jirachi", "Basic", "Prism Star"],
    subtypes=["Basic", "Prism Star"],
    collector_number=97,
    set_code="SM7",
    rarity=Rarities.Prism,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=385,
    abilities=[
        Ability(
            title="Wish Upon a Star",
            game_text="If you took this Pokémon as a face-down Prize card during your turn and your Bench isn't full, before you put it into your hand, you may put it onto your Bench and take 1 more Prize card.",
            trigger=Triggers.ON_TAKEN_AS_PRIZE,
            effect=wish_upon_a_star,
        ),
        Attack(
            title="Perish Dream",
            game_text="This Pokémon is now Asleep. At the end of your opponent's next turn, the Defending Pokémon will be Knocked Out.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            effect=perish_dream,
        ),
    ],
)
