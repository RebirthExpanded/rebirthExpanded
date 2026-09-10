"""Bunnelby (XY - Primal Clash 121/160).

Basic Colorless Pokemon. HP 60, weakness Fighting x2, no resistance,
retreat 2.

  Ancient Trait  Ω Barrage  This Pokemon may attack twice a turn. (If the
                            first attack Knocks Out your opponent's Active
                            Pokemon, you may attack again after your
                            opponent chooses a new Active Pokemon.)

  Burrow     [C]  Discard the top card of your opponent's deck.
  Rototiller [C]  Shuffle a card from your discard pile into your deck.

The pool's first Ancient Trait. It is NOT an Ability -- it is its own
line on the card, above the attacks -- so it goes in as an Ability entry
with ability_type=ANCIENT_TRAIT, which the client renders through its own
AncientTrait description class, and _collect_passives leaves it out of
what ability locks can reach: Garbotoxin, Silent Lab and Path to the Peak
each say "Abilities", and none of them touches this.

Ω Barrage is Jumpluff's Fluffy Barrage word for word, so both share
AttackTwicePassive. The wording matters against Festival Lead, which
repeats "an attack it HAS": this one says only "may attack twice", so a
Bunnelby holding Technical Machine: Evolution may use Evolution twice,
where Dipplin may not.

Both attacks are one Colorless and deal no damage. Burrow is mill_attack(1),
and Rototiller takes any card at all -- the pick is mandatory, and there is
nothing to choose only when the discard pile is empty.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import (AbilityTypes, PokemonTypes, PokemonStage,
                                    Rarities)
from spirit.game.card_effects.attacks_common import mill_attack
from spirit.game.card_effects.pokemon import AttackTwicePassive


async def rototiller(ctx):
    """Shuffle 1 card of your choice from your discard pile into your deck."""
    candidates = list(ctx.discard_pile())
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1,
        prompt="Choose a card to shuffle into your deck.",
    )
    if picks:
        await ctx.shuffle_into_deck(picks)


card = PokemonCardDef(
    guid="30ff41ad-3236-5efa-96df-8fba662e9be2",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bunnelby.Name",
    display_name="Bunnelby",
    searchable_by=["Bunnelby", "Basic", "Bunnelby"],
    subtypes=["Basic"],
    collector_number=121,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=659,
    abilities=[
        Ability(
            title="Ω Barrage",
            game_text="This Pokémon may attack twice a turn. (If the first attack Knocks Out your opponent's Active Pokémon, you may attack again after your opponent chooses a new Active Pokémon.)",
            ability_type=AbilityTypes.ANCIENT_TRAIT,
            passive=AttackTwicePassive(),
        ),
        Attack(
            title="Burrow",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=mill_attack(1),
        ),
        Attack(
            title="Rototiller",
            game_text="Shuffle a card from your discard pile into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=rototiller,
        ),
    ],
)
