"""Zarude (SVP 199 -- JP SVP 162; English SVP/199). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_grass(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.GRASS)


card = PokemonCardDef(
    guid="19c1f5e9-9ddd-5992-b2ef-5927c8641050",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zarude.Name",
    display_name="Zarude",
    searchable_by=["Zarude", "Basic"],
    subtypes=["Basic"],
    collector_number=199,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=893,
    abilities=[
        Attack(
            title="Pluck Off",
            game_text="Search your deck for up to 3 Basic [G] Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=su.search_to_hand(_basic_grass, count=3, reveal=True, prompt="Choose up to 3 Basic Grass Energy cards."),
        ),
        Attack(
            title="Hammer Whip",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.GRASS: 3},
            damage=130,
            effect=_hit_then_lock,
        ),
    ],
)
