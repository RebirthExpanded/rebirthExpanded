"""Banette ex (SV1 88 -- JP SV1V 041; English SVI/229, SVI/88). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_trainer_card, is_item_card


async def everlasting_darkness(ctx):
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, is_item_card)


async def poltergeist(ctx):
    hand = list(ctx.hand(ctx.opponent_id))
    if hand:
        await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    n = sum(1 for c in hand if is_trainer_card(c))
    if n:
        await ctx.deal_damage(60 * n)


card = PokemonCardDef(
    guid="616f4bea-a948-550f-a2d9-9c4f4bfd2fe6",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Banetteex.Name",
    display_name="Banette ex",
    searchable_by=["Banette ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=88,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    family_id=353,
    abilities=[
        Attack(
            title="Everlasting Darkness",
            game_text="During your opponent's next turn, they can't play any Item cards from their hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=everlasting_darkness,
        ),
        Attack(
            title="Poltergeist",
            game_text="Your opponent reveals their hand. This attack does 60 damage for each Trainer card you find there.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=poltergeist,
        ),
    ],
)
