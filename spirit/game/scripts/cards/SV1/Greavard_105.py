"""Greavard (SV1 105 -- JP SV1V 047; English SVI/105). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_supporter_card


async def underworld_stroll(ctx):
    hand = list(ctx.hand(ctx.opponent_id))
    if not hand:
        return
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    pool = [c for c in hand if is_supporter_card(c)]
    if pool:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Supporter card to put on the bottom of their deck")
        if picks:
            await ctx.put_on_bottom_of_deck(picks[0])


card = PokemonCardDef(
    guid="7dde84da-5d86-5773-94a2-5f6aacec1c15",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name",
    display_name="Greavard",
    searchable_by=["Greavard", "Basic"],
    subtypes=["Basic"],
    collector_number=105,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=971,
    abilities=[
        Attack(
            title="Underworld Stroll",
            game_text="Your opponent reveals their hand. Choose a Supporter card you find there and put it on the bottom of their deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=underworld_stroll,
        ),
        Attack(
            title="Sharp Fang",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
