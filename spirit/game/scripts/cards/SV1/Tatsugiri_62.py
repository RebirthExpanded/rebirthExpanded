"""Tatsugiri (SV1 62 -- JP SV1S 022; English PAF/127, SVI/62). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import full_stack


async def _back_to_hand(ctx):
    await ctx.deal_damage()
    me = ctx.attacker
    if me in ctx.knockouts:
        return
    if ctx.board.active_pokemon(ctx.player_id) is me and not ctx.my_bench():
        return
    await ctx.put_in_hand(full_stack(me), reveal=False)
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_water(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.WATER)

from spirit.game.session.effects import is_basic_pokemon_in_play


card = PokemonCardDef(
    guid="f8b3f07d-86e8-5513-9b9b-f3203dc7a246",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tatsugiri.Name",
    display_name="Tatsugiri",
    searchable_by=["Tatsugiri", "Basic"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=978,
    abilities=[
        Attack(
            title="Mise en Place",
            game_text="Search your deck for up to 2 Basic Water Energy cards and attach them to 1 of your Basic Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=su.search_attach_energy(_basic_water, count=2, target_pred=is_basic_pokemon_in_play, distribute=False, prompt="Choose up to 2 Basic Water Energy cards to attach to 1 of your Basic Pokémon."),
        ),
        Attack(
            title="Curl Up",
            game_text="Put this Pokémon and all attached cards into your hand.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=_back_to_hand,
        ),
    ],
)
