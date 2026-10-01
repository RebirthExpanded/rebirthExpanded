from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


def _defender_poisoned(ctx) -> bool:
    defender = ctx.defender
    return defender is not None and "Poisoned" in (defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


async def poison_absorption(ctx):
    """120; heal 100 from this Pokemon if the Defending Pokemon is Poisoned."""
    await ctx.deal_damage()
    if _defender_poisoned(ctx):
        await ctx.heal(100, ctx.attacker)


async def nasty_goo_mix(ctx):
    """Paralyzed and Poisoned; with at least 4 Energy attached (the attack
    costs none, so all of it is extra) the Poison is 15 counters."""
    counters = 15 if ctx.energy_units_on(ctx.attacker) >= 4 else 1
    await condition_attack(SpecialConditions.PARALYZED, SpecialConditions.POISONED,
                           counters=counters)(ctx)

card = PokemonCardDef(
    guid="4876db18-d8ba-5e93-aab3-6f876c8a0d08",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MukAlolanMukGX.Name",
    display_name="Muk & Alolan Muk-GX",
    searchable_by=["Muk & Alolan Muk-GX", "Basic", "TAG TEAM", "GX", "MukAlolanMukGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=61,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=89,
    abilities=[
        Attack(
            title="Severe Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. Put 8 damage counters instead of 1 on that Pok\u00e9mon between turns.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=0,
            effect=condition_attack(SpecialConditions.POISONED, counters=8),
        ),
        Attack(
            title="Poison Absorption",
            game_text="If your opponent's Active Pok\u00e9mon is Poisoned, heal 100 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=poison_absorption,
        ),
        Attack(
            title="Nasty Goo Mix-GX",
            game_text="Your opponent's Active Pok\u00e9mon is now Paralyzed and Poisoned. If this Pok\u00e9mon has at least 4 extra Energy attached to it (in addition to this attack's cost), put 15 damage counters instead of 1 on that Pok\u00e9mon between turns. (You can't use more than 1 GX attack in a game.)",
            cost={},
            damage=0,
            effect=nasty_goo_mix,
            gx=True,
        ),
    ],
)
