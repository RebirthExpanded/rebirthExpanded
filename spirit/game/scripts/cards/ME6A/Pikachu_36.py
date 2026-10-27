"""Pikachu (ME6A 36 -- JP M6a 036; English 30C/42). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card



async def charge_up_dash(ctx):
    heads = await ctx.flip_until_tails("Charge-Up Dash")
    if heads > 0:
        picks = await ctx.search_deck(lambda c: is_basic_energy_card(c) and is_energy_of_type(c, PokemonTypes.LIGHTNING),
                                      count=heads, minimum=0,
                                      prompt=f"Choose up to {heads} Basic Lightning Energy cards to attach to this Pokémon.")
        for energy in picks:
            await ctx.attach_energy(energy, ctx.attacker)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="f22686ef-8aac-50f0-8386-3a6243c75e8a",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Charge-Up Dash",
            game_text="Flip a coin until you get tails. Search your deck for an amount of Basic Lightning Energy up to the number of heads and attach it to this Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=charge_up_dash,
        ),
        Attack(
            title="Pika Bolt",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
