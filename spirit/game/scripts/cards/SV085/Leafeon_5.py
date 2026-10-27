"""Leafeon (SV085 5 -- JP SV5a 006; English PRE/5, SVP/170, TWM/11). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_grass(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.GRASS)
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def leaflet_blessings(ctx):
    pool = [c for c in ctx.hand() if _basic_grass(c)]
    bench = ctx.my_bench()
    if not pool or not bench:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Grass Energy card to attach")
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Pokémon") if picks else None
    if target is not None and await ctx.attach_energy(picks[0], target):
        n = _counters(ctx.board, target)
        if n:
            await ctx.heal(10 * n, target)


card = PokemonCardDef(
    guid="5d23c85b-c3aa-53b4-bdc9-4b46cd2e5c59",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Leafeon.Name",
    display_name="Leafeon",
    searchable_by=["Leafeon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Leaflet Blessings",
            game_text="Attach a Basic Grass Energy card from your hand to 1 of your Benched Pokémon. If you do, heal all damage from that Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=leaflet_blessings,
        ),
        Attack(
            title="Solar Beam",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
