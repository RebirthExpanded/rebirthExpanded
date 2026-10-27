"""Tropius (ME5 1 -- JP M5 001; English PBL/1). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


async def fruity_aroma(ctx):
    top = ctx.deck_top(6)
    if not top:
        return
    pool = [c for c in top if is_pokemon_card(c)]
    picks = await ctx.choose_cards(pool, len(pool), minimum=0, display_cards=top,
                                   prompt="Choose any number of Pokémon to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="635faddc-9a23-5dec-a508-eff6e7542d80",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tropius.Name",
    display_name="Tropius",
    searchable_by=["Tropius", "Basic"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=357,
    abilities=[
        Attack(
            title="Fruity Aroma",
            game_text="Look at the top 6 cards of your deck, and you may reveal any number of Pokémon you find there and put them into your hand. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=fruity_aroma,
        ),
        Attack(
            title="Solar Beam",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
