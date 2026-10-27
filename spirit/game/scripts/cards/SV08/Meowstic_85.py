"""Meowstic (SV08 85 -- JP SV8 054; English SSP/85). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.data_utils import def_for, subtypes_for


def _toy(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", "") == "Chill Teaser Toy"


def _beckoning_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    other = next((pid for pid in board.player_ids if pid != player_id), None)
    bench = board.find_player_area(other, "bench") if other else None
    return bool(hand) and any(_toy(c) for c in hand.children) and bool(bench and bench.children)


async def beckoning_tail(ctx):
    paid = await ctx.discard_from_hand(1, minimum=1, predicate=_toy, prompt="Discard a Chill Teaser Toy card to use Beckoning Tail.")
    bench = ctx.opponent_bench()
    if not paid or not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose the opponent's new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


card = PokemonCardDef(
    guid="766940df-aa46-5e6c-b71c-50228e1338a6",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowstic.Name",
    display_name="Meowstic",
    searchable_by=["Meowstic", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=85,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name",
    family_id=677,
    abilities=[
        Ability(
            title="Beckoning Tail",
            game_text="You must discard a Chill Teaser Toy card from your hand in order to use this Ability. Once during your turn, you may switch in 1 of your opponent's Benched Pokémon to the Active Spot.",
            activation=Activations.ONCE_PER_TURN,
            condition=_beckoning_condition,
            effect=beckoning_tail,
        ),
        Attack(
            title="Psyshot",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
