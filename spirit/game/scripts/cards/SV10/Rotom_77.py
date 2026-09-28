from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
import random
from spirit.game.session.effects import full_stack, is_pokemon_tool


async def astonish(ctx):
    """20, then a random card from the opponent's hand is revealed and
    shuffled into their deck."""
    await ctx.deal_damage()
    hand = list(ctx.hand(ctx.opponent_id))
    if not hand:
        return
    pick = random.choice(hand)
    await ctx.reveal_cards([pick])
    await ctx.shuffle_into_deck([pick], ctx.opponent_id)


async def gadget_show(ctx):
    """30 for each Pokemon Tool attached to all of your Pokemon."""
    tools = sum(1 for p in ctx.my_pokemon_in_play()
                for c in full_stack(p) if c is not p and is_pokemon_tool(c))
    if tools:
        await ctx.deal_damage(30 * tools)

card = PokemonCardDef(
    guid="75618775-716b-55e9-8afb-a7c125af4118",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name",
    display_name="Rotom",
    searchable_by=["Rotom", "Basic", "Rotom"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=479,
    abilities=[
        Attack(
            title="Astonish",
            game_text="Choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into their deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=astonish,
        ),
        Attack(
            title="Gadget Show",
            game_text="This attack does 30 damage for each Pok\u00e9mon Tool attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=gadget_show,
        ),
    ],
)
