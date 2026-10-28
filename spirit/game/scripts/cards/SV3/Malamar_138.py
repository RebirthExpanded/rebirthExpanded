"""Malamar (SV3 138 -- JP SV3 076; English OBF/138). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


def _insight_condition(board, player_id, pokemon) -> bool:
    other = next((pid for pid in board.player_ids if pid != player_id), None)
    deck = board.find_player_area(other, "deck") if other else None
    return bool(deck and deck.children)


async def psychic_insight(ctx):
    theirs = list(ctx.deck_top(1, player_id=ctx.opponent_id))
    if not theirs:
        return
    await ctx.reveal_cards(theirs, to_player=ctx.player_id)
    mine = list(ctx.deck_top(1))
    if mine:
        await ctx.reveal_cards(mine, to_player=ctx.player_id)


card = PokemonCardDef(
    guid="ae92d306-c81c-58fd-a05a-323d4ae90760",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Malamar.Name",
    display_name="Malamar",
    searchable_by=["Malamar", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=138,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    family_id=686,
    abilities=[
        Ability(
            title="Psychic Insight",
            game_text="Once during your turn, you may look at the top card of your opponent's deck. If you do, look at the top card of your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_insight_condition,
            effect=psychic_insight,
        ),
        Attack(
            title="Hypnotic Ray",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
