"""Pikachu (ME6A 37 -- JP M6a 037; English 30C/43). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


async def tropical_vibes(ctx):
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)
    await ctx.draw_until(6)


card = PokemonCardDef(
    guid="83f2c84a-51f7-5b83-8f69-0e1df3bf8ba2",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Tropical Vibes",
            game_text="This Pokémon is now Asleep. Draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=tropical_vibes,
        ),
    ],
)
