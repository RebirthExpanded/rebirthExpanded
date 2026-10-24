"""Alakazam-EX (XY - Fates Collide 117/122).

Basic Psychic Pokemon-EX. HP 160, weakness Psychic x2, retreat 2.

  Kinesis  (Ability)  When you play M Alakazam-EX from your hand to evolve
                      this Pokemon, before it evolves, you may put 2 damage
                      counters on your opponent's Active Pokemon and 3 on 1
                      of their Benched Pokemon.
  Suppression  [PC]  3 damage counters on each of the opponent's Pokemon
                     that has any Energy attached.

Triggers.ON_BEING_EVOLVED: the evolve executor fires it on this Pokemon
before M Alakazam-EX goes on top (ctx.evolution_card is the card in hand).
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for


def _evolving_into_mega(ctx) -> bool:
    evo = getattr(ctx, "evolution_card", None)
    return evo is not None and getattr(def_for(evo.archetype_id), "display_name", None) == "M Alakazam-EX"


async def _kinesis(ctx):
    """When you play M Alakazam-EX from hand to evolve this Pokemon, before it
    evolves: you may put 2 counters on the opponent's Active and 3 on 1 of their Benched."""
    evo = getattr(ctx, "evolution_card", None)
    if evo is None or getattr(def_for(evo.archetype_id), "display_name", None) != "M Alakazam-EX":
        return
    if not await ctx.ask_yes_no("Use Kinesis?"):
        return
    d = ctx.opponent_active()
    if d is not None:
        await ctx.place_damage_counters(2, [d])
    bench = ctx.opponent_bench()
    if bench:
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(bench, "Put 3 damage counters on which Benched Pokémon?")
        if target is not None:
            await ctx.place_damage_counters(3, [target])


async def _suppression(ctx):
    """Put 3 damage counters on each of your opponent's Pokemon that has any Energy attached."""
    for p in list(ctx.opponent_pokemon_in_play()):
        if ctx.attached_energies(p):
            await ctx.place_damage_counters(3, [p])


card = PokemonCardDef(
    guid="a52adcfb-baa4-5b52-888f-6b478ce00a37",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlakazamEX.Name",
    display_name="Alakazam-EX",
    searchable_by=["Alakazam-EX", "Basic", "EX", "AlakazamEX"],
    subtypes=["Basic", "EX"],
    collector_number=117,
    set_code="XY10",
    rarity=Rarities.RareUltra,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=65,
    abilities=[
        Ability(
            title="Kinesis",
            game_text="When you play M Alakazam-EX from your hand to evolve this Pok\u00e9mon, before it evolves, you may put 2 damage counters on your opponent's Active Pok\u00e9mon and 3 damage counters on 1 of your opponent's Benched Pok\u00e9mon.",
            trigger=Triggers.ON_BEING_EVOLVED,
            trigger_applies=_evolving_into_mega,
            effect=_kinesis,
        ),
        Attack(
            title="Suppression",
            game_text="Put 3 damage counters on each of your opponent's Pok\u00e9mon that has any Energy attached to it.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=_suppression,
        ),
    ],
)