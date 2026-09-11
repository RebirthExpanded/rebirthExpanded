"""Jirachi (XY Black Star Promos XY67 -- JP "THE BEST OF XY" 080/171).

Basic Metal Pokemon. HP 60, weakness Fire x2, resistance Psychic -20,
retreat 1.

  Stardust     [C] 10   Discard a Special Energy attached to your opponent's
                        Active Pokemon. If you do, prevent all effects of
                        attacks, including damage, done to this Pokemon
                        during your opponent's next turn.
  Dream Dance  [MC] 20  Both Active Pokemon are now Asleep.

"If you do" is a real gate: no Special Energy over there (or a Defending
Pokemon shielded from attack effects) means no shield for this Pokemon
either, so the attack is 10 damage and nothing else.
"""

from spirit.game.attributes import (PokemonStage, PokemonTypes, Rarities,
                                    SpecialConditions)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import apply_protection
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_special_energy


async def stardust(ctx):
    """10, a Special Energy off their Active, and a shield if one went."""
    await ctx.deal_damage()
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    discarded = await ctx.discard_energy_from(
        target, 1, predicate=is_special_energy,
        prompt="Choose a Special Energy to discard from the Defending Pokémon")
    if not discarded:
        return
    await apply_protection(ctx, target=ctx.attacker, prevent=True,
                           effects_too=True)


card = PokemonCardDef(
    guid="64e33cd0-cb84-5470-80fd-bcfcbc5e9cd0",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi",
    searchable_by=["Jirachi", "Basic"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=385,
    abilities=[
        Attack(
            title="Stardust",
            game_text="Discard a Special Energy attached to your opponent's Active Pokémon. If you do, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=stardust,
        ),
        Attack(
            title="Dream Dance",
            game_text="Both Active Pokémon are now Asleep.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.ASLEEP,
                                    both_actives=True),
        ),
    ],
)
