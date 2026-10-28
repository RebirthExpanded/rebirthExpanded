"""Dondozo (SV4 55 -- JP SV3a 011; English PAR/55). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card


async def supplemental_swallow_up(ctx):
    top = list(ctx.deck_top(5))
    if not top:
        return
    await ctx.reveal_cards(top, to_player=ctx.player_id)
    pool = [c for c in top if is_basic_energy_card(c)]
    if pool:
        picks = await ctx.choose_cards(pool, len(pool), minimum=0, prompt="Attach any number of Basic Energy cards to this Pokémon")
        for card in picks:
            await ctx.attach_energy(card, ctx.attacker)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="015fe93e-40df-5cda-b930-ce7b6ed50771",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dondozo.Name",
    display_name="Dondozo",
    searchable_by=["Dondozo", "Basic"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=977,
    abilities=[
        Attack(
            title="Supplemental Swallow-Up",
            game_text="Look at the top 5 cards of your deck. You may attach any number of Basic Energy cards you find there to this Pokémon. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=supplemental_swallow_up,
        ),
        Attack(
            title="Hydro Splash",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 4},
            damage=180,
        ),
    ],
)
