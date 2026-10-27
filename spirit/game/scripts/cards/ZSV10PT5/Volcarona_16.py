"""Volcarona (ZSV10PT5 16 -- JP SV11B 019; English BLK/100, BLK/16). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fire(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIRE)



def _torrid_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(_basic_fire(c) for c in hand.children)


async def torrid_scales(ctx):
    paid = await ctx.discard_from_hand(1, minimum=1, predicate=_basic_fire,
                                       prompt="Discard a Basic Fire Energy card to use Torrid Scales.")
    target = ctx.opponent_active()
    if paid and target is not None:
        await ctx.apply_special_condition(target, SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="d9006d0d-1c3c-5dcf-aeac-596063f051a5",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcarona.Name",
    display_name="Volcarona",
    searchable_by=["Volcarona", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    family_id=636,
    abilities=[
        Ability(
            title="Torrid Scales",
            game_text="You must discard a Basic Fire Energy card from your hand in order to use this Ability. Once during your turn, you may make your opponent's Active Pokémon Burned.",
            activation=Activations.ONCE_PER_TURN,
            condition=_torrid_condition,
            effect=torrid_scales,
        ),
        Attack(
            title="Fire Wing",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
