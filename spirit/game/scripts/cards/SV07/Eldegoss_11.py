"""Eldegoss (SV07 11 -- JP SV7 009; English SCR/11). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import full_stack


async def breezy_gift(ctx):
    me = ctx.attacker
    if ctx.board.active_pokemon(ctx.player_id) is me and not ctx.my_bench():
        return
    await ctx.shuffle_into_deck(full_stack(me), ctx.player_id)
    picks = await ctx.search_deck(count=3, minimum=0, prompt="Choose up to 3 cards to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="4d496b74-15fd-52da-92a5-a032d76902c4",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eldegoss.Name",
    display_name="Eldegoss",
    searchable_by=["Eldegoss", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gossifleur.Name",
    family_id=829,
    abilities=[
        Attack(
            title="Breezy Gift",
            game_text="Put this Pokémon and all attached cards into your deck. If you do, search your deck for up to 3 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=breezy_gift,
        ),
        Attack(
            title="Leafage",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
        ),
    ],
)
