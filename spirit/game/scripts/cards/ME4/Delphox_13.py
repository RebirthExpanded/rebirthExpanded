"""Delphox (ME4 13 -- JP M4 013; English CRI/13, MEP/74). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fire(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIRE)



def _flaring_ok(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return any(_basic_fire(c) for c in (hand.children if hand else []))


async def flaring_magic(ctx):
    paid = await ctx.discard_from_hand(1, minimum=1, predicate=_basic_fire,
                                       prompt="Discard a Basic Fire Energy card to use Flaring Magic.")
    if paid:
        await ctx.draw_until(7)


card = PokemonCardDef(
    guid="ab3baaef-2e8f-5ddf-994e-dadadcb75044",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delphox.Name",
    display_name="Delphox",
    searchable_by=["Delphox", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name",
    family_id=653,
    abilities=[
        Ability(
            title="Flaring Magic",
            game_text="Once during your turn, you may discard a Basic Fire Energy card from your hand in order to use this Ability. Draw cards until you have 7 cards in your hand.",
            activation=Activations.ONCE_PER_TURN,
            condition=_flaring_ok,
            effect=flaring_magic,
        ),
        Attack(
            title="Energized Storm",
            game_text="This attack does 30 damage for each Energy attached to all Pokémon.",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            damage_operator="x",
            effect=ac.damage_per(ac.count_energy("both"), 30),
        ),
    ],
)
