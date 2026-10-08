"""Guzzlord (SM - Cosmic Eclipse 136/236 -- JP SM11a 046/064, the art here).

Basic Darkness Pokemon. HP 150, weakness Fighting x2, resistance Psychic
-20, retreat 4.

  Mountain Munch [D]       Discard the top card of your opponent's deck.
  Red Banquet    [DDCC] 120  If your opponent's Pokemon is Knocked Out by
                             damage from this attack, take 1 more Prize
                             card.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import mill_attack
from spirit.game.data_utils import Attack, PokemonCardDef


async def red_banquet(ctx):
    defender = ctx.defender
    await ctx.deal_damage()
    if defender is not None and defender in ctx.knockouts:
        ctx.extra_prizes += 1


card = PokemonCardDef(
    guid="22f7c514-4585-520f-8bd7-f9cef7f8e4a4",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Guzzlord.Name",
    display_name="Guzzlord",
    searchable_by=["Guzzlord", "Basic", "Ultra Beast"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=136,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=799,
    abilities=[
        Attack(
            title="Mountain Munch",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=mill_attack(1),
        ),
        Attack(
            title="Red Banquet",
            game_text="If your opponent's Pokémon is Knocked Out by damage from this attack, take 1 more Prize card.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=red_banquet,
        ),
    ],
)
