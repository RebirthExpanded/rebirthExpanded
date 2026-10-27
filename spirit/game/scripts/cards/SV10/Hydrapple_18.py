"""Hydrapple (SV10 18 -- JP SV9a 011; English DRI/18, DRI/188). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_grass(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.GRASS)


async def hydra_breath(ctx):
    pool = [c for c in ctx.hand() if _basic_grass(c)]
    if len(pool) < 6:
        return
    paid = await ctx.discard_from_hand(6, minimum=6, predicate=_basic_grass,
                                       prompt="Discard 6 Basic Grass Energy cards from your hand.")
    target = ctx.opponent_active()
    if len(paid) >= 6 and target is not None:
        await ctx.knock_out(target)


card = PokemonCardDef(
    guid="46cc19e2-f47a-5b09-a317-4046fca54193",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydrapple.Name",
    display_name="Hydrapple",
    searchable_by=["Hydrapple", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=18,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dipplin.Name",
    family_id=840,
    abilities=[
        Attack(
            title="Hydra Breath",
            game_text="Discard 6 Basic Grass Energy cards from your hand, and Knock Out your opponent's Active Pokémon. If you can't discard 6 cards in this way, this attack does nothing.",
            cost={PokemonTypes.GRASS: 1},
            effect=hydra_breath,
        ),
        Attack(
            title="Whip Smash",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
        ),
    ],
)
