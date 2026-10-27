"""Lurantis (SV10 14 -- JP SV10 006; English DRI/14). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_grass(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.GRASS)


async def petal_blade_dance(ctx):
    pool = [c for c in ctx.hand() if _basic_grass(c)]
    if len(pool) < 2:
        return
    paid = await ctx.discard_from_hand(2, minimum=2, predicate=_basic_grass,
                                       prompt="Discard 2 Basic Grass Energy cards from your hand.")
    if len(paid) >= 2:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="d0633978-1f4c-5fad-a33f-1ea629799428",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lurantis.Name",
    display_name="Lurantis",
    searchable_by=["Lurantis", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fomantis.Name",
    family_id=753,
    abilities=[
        Attack(
            title="Razor Leaf",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Petal Blade Dance",
            game_text="Discard 2 Basic Grass Energy cards from your hand. If you can't discard 2 cards in this way, this attack does nothing.",
            cost={PokemonTypes.GRASS: 1},
            damage=130,
            effect=petal_blade_dance,
        ),
    ],
)
