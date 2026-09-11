"""Wobbuffet BREAK (XY Black Star Promos XY155 -- JP CP4 020/131).

BREAK Evolution of Wobbuffet, Psychic. HP 140.

  BREAK Evolution rule: Wobbuffet BREAK retains the attacks, Abilities,
  Weakness, Resistance, and Retreat Cost of its previous Evolution.

  Right Back at You  [PC]  Discard all Energy attached to this Pokemon.
                           During your opponent's next turn, if this
                           Pokemon is damaged by an attack (even if this
                           Pokemon is Knocked Out), put damage counters on
                           the Attacking Pokemon equal to the damage done
                           to this Pokemon.

The pool's first BREAK Evolution, so the rule box comes with it:

* It evolves like any Evolution -- evolves_from names Wobbuffet, and the
  name match is what every evolution path reads, so Boost Shake, Wally and
  Technical Machine: Evolution all reach it. Grand Tree asks for "a Stage
  1 or Stage 2 card" and does not. Rare Candy wants a Stage 2 and does not.
* "Retains the attacks, Abilities, Weakness, Resistance, and Retreat
  Cost": on evolving, the BREAK takes over the previous Evolution's
  Weakness/Resistance/Retreat attributes (and hands them back when it
  leaves play), and its PIE_ABILITIES carry the previous Evolution's
  attacks and Abilities beside its own -- so Bide Barricade keeps working
  with the BREAK on top, rides the BREAK as its carrier, and still answers
  to ability locks. Which Wobbuffet it retains from is read off the stack,
  so a Single Strike Wobbuffet underneath gives it that card's stats.
* It prints a rule, so it is a "Pokemon with a Rule Box" (has_rule_box),
  while staying worth 1 Prize.

Right Back at You is Aggron's Counter Press with the Energy discard in
front: a damage interceptor that lives through the opponent's next turn,
placing the counters BEFORE the HP write, which is what "even if this
Pokemon is Knocked Out" needs.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.passives import Passive


class RightBackAtYouPassive(Passive):
    """Damage taken from an attack comes back as counters on the attacker."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if target is not carrier:
            return None
        attacker = calc.attacker
        if attacker is not None:
            await ctx.deal_damage(calc.amount, target=attacker,
                                  apply_modifiers=False, as_counters=True)
        return None


async def right_back_at_you(ctx):
    """Shed every Energy, then reflect next turn's hits as counters."""
    await ctx.discard_energy_from(
        ctx.attacker, 99, prompt="Discard all Energy from this Pokémon")
    ctx.add_passive_through_opponents_turn(ctx.attacker, RightBackAtYouPassive())


card = PokemonCardDef(
    guid="bb0e56f6-834d-5dd3-b4a8-1beda72c7356",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WobbuffetBREAK.Name",
    display_name="Wobbuffet BREAK",
    searchable_by=["Wobbuffet BREAK", "BREAK", "WobbuffetBREAK"],
    subtypes=["BREAK"],
    collector_number=155,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name",
    family_id=202,
    abilities=[
        Attack(
            title="Right Back at You",
            game_text="Discard all Energy attached to this Pokémon. During your opponent's next turn, if this Pokémon is damaged by an attack (even if this Pokémon is Knocked Out), put damage counters on the Attacking Pokémon equal to the damage done to this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=right_back_at_you,
        ),
    ],
)
