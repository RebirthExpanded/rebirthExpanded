"""Greedent ex (SV3 179 -- JP SVD 100; English OBF/179). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

async def never_ever_enough(ctx):
    top = list(ctx.deck_top(3))
    if not top:
        return
    await ctx.reveal_cards(top, to_player=ctx.player_id)
    if await ctx.ask_yes_no("Put those cards into your hand? (No: discard them and draw 3 cards)"):
        await ctx.put_in_hand(top, reveal=False)
    else:
        await ctx.discard_cards(top)
        await ctx.draw_cards(3)


card = PokemonCardDef(
    guid="b5330ba8-04b9-59b5-8755-287688634256",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greedentex.Name",
    display_name="Greedent ex",
    searchable_by=["Greedent ex", "Stage 1", "ex", "Tera"],
    subtypes=["Stage 1", "ex", "Tera"],
    collector_number=179,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skwovet.Name",
    family_id=819,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Never Ever Enough",
            game_text="Look at the top 3 cards of your deck. You may put those cards into your hand. If you don't, discard those cards and draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=never_ever_enough,
        ),
        Attack(
            title="Slip 'n' Roll",
            game_text="During your next turn, this Pokémon can't use Slip 'n' Roll.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=210,
            locks_next_turn=True,
        ),
    ],
)
