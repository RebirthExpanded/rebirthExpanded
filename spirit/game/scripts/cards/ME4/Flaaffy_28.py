"""Flaaffy (ME - CRI 28 -- JP M4 028, the art here).

Stage 1 Lightning Pokemon, evolves from Mareep. HP 90, weakness Fighting
x2, no resistance, retreat 2.

  Disconnect [LC] 40  During your opponent's next turn, they can't play any
                      Item cards from their hand.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_item_card


async def disconnect(ctx):
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, is_item_card)


card = PokemonCardDef(
    guid="e09bab5a-7645-5dcd-83f0-929516de71f4",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    display_name="Flaaffy",
    searchable_by=["Flaaffy", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name",
    family_id=179,
    abilities=[
        Attack(title="Disconnect",
               game_text="During your opponent's next turn, they can't play any Item cards from their hand.",
               cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
               damage=40, effect=disconnect),
    ],
)
