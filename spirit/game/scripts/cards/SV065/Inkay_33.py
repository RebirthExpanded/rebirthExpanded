"""Inkay (SV065 33 -- JP SV6a 033; English SFA/33). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def mischievous_tentacles(ctx):
    top = list(ctx.deck_top(1, player_id=ctx.opponent_id))
    if not top:
        return
    await ctx.reveal_cards(top, to_player=ctx.player_id)
    if await ctx.ask_yes_no("Have your opponent shuffle their deck?"):
        await ctx.shuffle_deck(ctx.opponent_id)


card = PokemonCardDef(
    guid="4e82b940-b522-59ef-88ce-4e9f33e3a267",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    display_name="Inkay",
    searchable_by=["Inkay", "Basic"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=686,
    abilities=[
        Attack(
            title="Mischievous Tentacles",
            game_text="Look at the top card of your opponent's deck. You may have your opponent shuffle their deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=mischievous_tentacles,
        ),
        Attack(
            title="Peck",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)
