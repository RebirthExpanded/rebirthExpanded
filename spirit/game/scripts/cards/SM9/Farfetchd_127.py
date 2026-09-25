"""Farfetch'd (SM - Team Up 127/181 -- JP SM9 073/095).

Basic Colorless Pokemon. HP 80, weakness Lightning x2, resistance
Fighting -20, retreat 1.

  Collect      [C]     Draw 2 cards.
  Tool Buster  [C] 20+ Before doing damage, discard all Pokemon Tool cards
                       from your opponent's Active Pokemon. If you discarded
                       a Pokemon Tool card in this way, this attack does 70
                       more damage.

The bonus reads what actually left: a Tool the effect cannot discard (the
Active is protected from attack effects) earns nothing.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.data_utils import Attack, PokemonCardDef


async def tool_buster(ctx):
    target = ctx.defender
    discarded = 0
    if target is not None and not ctx.effects_blocked(target):
        tools = [t for t, p in ctx.tools_in_play() if p is target]
        if tools:
            await ctx.discard_cards(tools)
            discarded = sum(1 for t in tools if t.parent is not target)
    await ctx.deal_damage(20 + (70 if discarded else 0))


card = PokemonCardDef(
    guid="ff2ee8c5-874d-537a-80d5-2bcc1816a95c",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Farfetchd.Name",
    display_name="Farfetch'd",
    searchable_by=["Farfetch'd", "Basic", "Farfetchd"],
    subtypes=["Basic"],
    collector_number=127,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=83,
    abilities=[
        Attack(title="Collect", game_text="Draw 2 cards.",
               cost={PokemonTypes.COLORLESS: 1}, damage=0,
               effect=draw_attack(2)),
        Attack(title="Tool Buster",
               game_text="Before doing damage, discard all Pokémon Tool cards from your opponent's Active Pokémon. If you discarded a Pokémon Tool card in this way, this attack does 70 more damage.",
               cost={PokemonTypes.COLORLESS: 1}, damage=20, damage_operator="+",
               effect=tool_buster),
    ],
)
