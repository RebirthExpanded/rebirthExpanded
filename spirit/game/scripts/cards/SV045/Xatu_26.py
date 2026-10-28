"""Xatu (SV045 26 -- JP SVEM 005; English PAF/152, PAF/26, PAR/72, SVP/59). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_psychic(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.PSYCHIC)


def _sense_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    bench = board.find_player_area(player_id, "bench")
    return bool(hand and bench and bench.children) and any(_basic_psychic(c) for c in hand.children)


async def clairvoyant_sense(ctx):
    pool = [c for c in ctx.hand() if _basic_psychic(c)]
    bench = ctx.my_bench()
    if not pool or not bench:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Psychic Energy card")
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Pokémon") if picks else None
    if target is not None and await ctx.attach_energy(picks[0], target):
        await ctx.draw_cards(2)


card = PokemonCardDef(
    guid="d05ccdde-201e-5b29-9017-8f32a8b2b067",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xatu.Name",
    display_name="Xatu",
    searchable_by=["Xatu", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    family_id=177,
    abilities=[
        Ability(
            title="Clairvoyant Sense",
            game_text="Once during your turn, you may attach a Basic Psychic Energy card from your hand to 1 of your Benched Pokémon. If you attached Energy to a Pokémon in this way, draw 2 cards.",
            activation=Activations.ONCE_PER_TURN,
            condition=_sense_condition,
            effect=clairvoyant_sense,
        ),
        Attack(
            title="Super Psy Bolt",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
