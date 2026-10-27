"""Eternatus (ME2 69 -- JP MBG 008; English PFL/69). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def shatter(ctx):
    await ctx.deal_damage()
    if ctx.stadium_in_play() is not None:
        await ctx.discard_stadium()


async def power_rush(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Power Rush")
    if results and not results[0]:
        ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="36b84997-56db-5a4c-a702-ea11ffd2b003",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eternatus.Name",
    display_name="Eternatus",
    searchable_by=["Eternatus", "Basic"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=890,
    abilities=[
        Attack(
            title="Shatter",
            game_text="Discard a Stadium in play.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=50,
            effect=shatter,
        ),
        Attack(
            title="Power Rush",
            game_text="Flip a coin. If tails, during your next turn, this Pokémon can't use attacks.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=130,
            effect=power_rush,
        ),
    ],
)
