"""Pidove (ZSV10PT5 71 -- JP SV11B 073; English BLK/148, BLK/71). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def scout(ctx):
    if ctx.hand(ctx.opponent_id):
        await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)


card = PokemonCardDef(
    guid="6fb8c87b-8cb4-5eff-9b0f-5b16be14fdae",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidove.Name",
    display_name="Pidove",
    searchable_by=["Pidove", "Basic"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=519,
    abilities=[
        Attack(
            title="Scout",
            game_text="Your opponent reveals their hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=scout,
        ),
        Attack(
            title="Stampede",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
