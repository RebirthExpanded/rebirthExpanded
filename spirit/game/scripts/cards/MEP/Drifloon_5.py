"""Drifloon (MEP 5 -- JP SVP 234; English MEP/5). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


async def pull(ctx):
    results = await ctx.flip_coins(1, "Pull")
    if results and results[0]:
        await su.gust_attack()(ctx)


card = PokemonCardDef(
    guid="4274607f-3aa0-53bc-9a59-9934b83e46ff",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    display_name="Drifloon",
    searchable_by=["Drifloon", "Basic"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="MEP",
    regulation_mark="I",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=425,
    abilities=[
        Attack(
            title="Pull",
            game_text="Flip a coin. If heads, switch in 1 of your opponent's Benched Pokémon to the Active Spot.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=pull,
        ),
    ],
)
