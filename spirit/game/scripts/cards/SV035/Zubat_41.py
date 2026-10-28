"""Zubat (SV035 41 -- JP SV2a 041; English MEW/41). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

def _echo_condition(board, player_id, pokemon) -> bool:
    other = next((pid for pid in board.player_ids if pid != player_id), None)
    hand = board.find_player_area(other, "hand") if other else None
    return board.active_pokemon(player_id) is pokemon and bool(hand and hand.children)


async def revealing_echo(ctx):
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)


card = PokemonCardDef(
    guid="6ff7d110-e93f-5b00-b82d-788daaeecfd9",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name",
    display_name="Zubat",
    searchable_by=["Zubat", "Basic"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=41,
    abilities=[
        Ability(
            title="Revealing Echo",
            game_text="Once during your turn, if this Pokémon is in the Active Spot, you may have your opponent reveal their hand.",
            activation=Activations.ONCE_PER_TURN,
            condition=_echo_condition,
            effect=revealing_echo,
        ),
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
