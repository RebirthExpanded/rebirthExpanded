"""Iron Hands ex (SV - Paradox Rift 70/182 -- JP SV4M 027/066).

Basic Lightning Pokemon ex (Future). HP 230, weakness Fighting x2,
retreat 4.

  Arm Press  [LLC] 160
  Amp You Very Much  [LCCC] 120  If your opponent's Pokemon is Knocked Out
                                 by damage from this attack, take 1 more
                                 Prize card.

The extra Prize rides a this-turn watcher keyed on this attacker, so the
KO must come from this attack's damage (a Bench KO by this attack's
damage would count too; a KO by an effect or by Poison would not).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef


async def amp_you_very_much(ctx):
    attacker = ctx.attacker
    ctx.add_extra_prize_watcher(attacker_predicate=lambda p: p is attacker, prizes=1)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="a953a8bc-1176-558a-9e24-8293e541fbcf",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronHandsex.Name",
    display_name="Iron Hands ex",
    searchable_by=["Iron Hands ex", "Basic", "ex", "Future", "IronHandsex"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=70,
    set_code="SV4",
    rarity=Rarities.RareUltra,
    hp=230,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=992,
    regulation_mark="G",
    abilities=[
        Attack(title="Arm Press", game_text="",
               cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1}, damage=160),
        Attack(
            title="Amp You Very Much",
            game_text="If your opponent's Pokémon is Knocked Out by damage from this attack, take 1 more Prize card.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=amp_you_very_much,
        ),
    ],
)
