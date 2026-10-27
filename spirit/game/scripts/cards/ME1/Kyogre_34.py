"""Kyogre (ME1 34 -- JP M1S 016; English MEG/34). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_water(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.WATER)


async def riptide(ctx):
    pool = [c for c in ctx.discard_pile() if _basic_water(c)]
    if pool:
        await ctx.deal_damage(20 * len(pool))
        await ctx.shuffle_into_deck(pool, ctx.player_id)


card = PokemonCardDef(
    guid="f15be339-ffaa-506e-99b8-b11e2969627f",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogre.Name",
    display_name="Kyogre",
    searchable_by=["Kyogre", "Basic"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Attack(
            title="Riptide",
            game_text="This attack does 20 damage for each Basic Water Energy card in your discard pile. Then, shuffle those cards into your deck.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            damage_operator="x",
            effect=riptide,
        ),
        Attack(
            title="Swirling Waves",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=ac.self_energy_discard_attack(count=2),
        ),
    ],
)
