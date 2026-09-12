"""Luxio (SM - Ultra Prism 47/156 -- JP SM5M 019/066, the art here).

Stage 1 Lightning Pokemon, evolves from Shinx. HP 80, weakness Fighting x2,
resistance Metal -20, retreat 1.

  Disconnect [C] 30  Your opponent can't play any Item cards from their
                     hand during their next turn.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_item_card


async def disconnect(ctx):
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, is_item_card)


card = PokemonCardDef(
    guid="079a5d32-f18d-51b2-9ef7-48ef46dacf6b",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    display_name="Luxio",
    searchable_by=["Luxio", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name",
    family_id=403,
    abilities=[
        Attack(title="Disconnect",
               game_text="Your opponent can't play any Item cards from their hand during their next turn.",
               cost={PokemonTypes.COLORLESS: 1},
               damage=30, effect=disconnect),
    ],
)
