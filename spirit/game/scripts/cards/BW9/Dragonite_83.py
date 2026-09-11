"""Dragonite (BW - Plasma Freeze 83/116 -- JP BW8-Brn 040/076).

Stage 2 Dragon Pokemon, evolves from Dragonair. HP 150, weakness Dragon
x2, retreat 3.

  Deafen    [CCC] 60   Your opponent can't play any Item cards from their
                       hand during their next turn.
  Healwing  [GLCC] 90  Heal 30 damage from this Pokemon.

Deafen's lock is an effect of an attack on the opponent: Pokemon Ranger
lifts it and Marowak's Bodyguard keeps it off.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_item_card


async def deafen(ctx):
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, is_item_card)


async def healwing(ctx):
    await ctx.deal_damage()
    await ctx.heal(30, ctx.attacker)


card = PokemonCardDef(
    guid="dce55f81-099d-5b6e-9117-6300d739fc37",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name",
    display_name="Dragonite",
    searchable_by=["Dragonite", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=83,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=147,
    abilities=[
        Attack(
            title="Deafen",
            game_text="Your opponent can't play any Item cards from their hand during their next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=deafen,
        ),
        Attack(
            title="Healwing",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=healwing,
        ),
    ],
)
