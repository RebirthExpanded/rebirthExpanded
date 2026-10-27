"""Archeops (RSV10PT5 51 -- JP SV11W 048; English WHT/132, WHT/51). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc

from spirit.game.session.effects import is_evolution_pokemon


def _ancient_wing_condition(board, player_id, pokemon) -> bool:
    if board.active_pokemon(player_id) is not pokemon:
        return False
    other = next((pid for pid in board.player_ids if pid != player_id), None)
    return any(is_evolution_pokemon(p) for p in board.pokemon_in_play(other)) if other else False


async def ancient_wing(ctx):
    pool = [p for p in ctx.opponent_pokemon_in_play() if is_evolution_pokemon(p)]
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's evolved Pokémon to devolve")
    if target is not None:
        await ctx.devolve_pokemon(target, 1, "hand")


card = PokemonCardDef(
    guid="cbb94280-da69-5912-9369-7ca657d22992",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archeops.Name",
    display_name="Archeops",
    searchable_by=["Archeops", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=51,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Archen.Name",
    family_id=566,
    abilities=[
        Ability(
            title="Ancient Wing",
            game_text="Once during your turn, if this Pokémon is in the Active Spot, you may devolve 1 of your opponent's evolved Pokémon by putting the highest Stage Evolution card on it into your opponent's hand.",
            activation=Activations.ONCE_PER_TURN,
            condition=_ancient_wing_condition,
            effect=ancient_wing,
        ),
        Attack(
            title="Rock Throw",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
