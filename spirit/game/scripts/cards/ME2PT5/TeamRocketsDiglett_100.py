"""Team Rocket's Diglett (ME2PT5 100 -- JP M2a 082; English ASC/100). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def relentless_burrowing(ctx):
    heads = await ctx.flip_until_tails("Relentless Burrowing")
    top = list(ctx.deck_top(heads, player_id=ctx.opponent_id)) if heads else []
    if top:
        await ctx.discard_cards(top)


card = PokemonCardDef(
    guid="4cf71fdc-ebac-5e6c-8a78-95f597da5358",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsDiglett.Name",
    display_name="Team Rocket's Diglett",
    searchable_by=["Team Rocket's Diglett", "Basic"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=50,
    abilities=[
        Attack(
            title="Relentless Burrowing",
            game_text="Flip a coin until you get tails. For each heads, discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=relentless_burrowing,
        ),
    ],
)
