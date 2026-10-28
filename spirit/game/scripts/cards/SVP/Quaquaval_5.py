"""Quaquaval (SVP 5 -- JP SVAW 004; English SVI/54, SVP/5). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card


def _carnival_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(is_basic_energy_card(c) for c in hand.children)


async def energy_carnival(ctx):
    pool = [c for c in ctx.hand() if is_basic_energy_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Energy card to attach")
    target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon") if picks else None
    if target is not None:
        await ctx.attach_energy(picks[0], target)


card = PokemonCardDef(
    guid="f53c6210-e794-5fa0-a507-13a0edde7558",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quaquaval.Name",
    display_name="Quaquaval",
    searchable_by=["Quaquaval", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quaxwell.Name",
    family_id=912,
    abilities=[
        Ability(
            title="Energy Carnival",
            game_text="Once during your turn, you may attach a Basic Energy card from your hand to 1 of your Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_carnival_condition,
            effect=energy_carnival,
        ),
        Attack(
            title="Hydro Kick",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
        ),
    ],
)
