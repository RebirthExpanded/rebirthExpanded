"""Pretend Plasma Boss Pikachu (SMPJ 195 -- JP SMP 195; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_pokemon_card


async def _liberate(ctx):
    """Look at the opponent's hand and discard a Pokemon you find there."""
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    pokemon = [c for c in (hand or ctx.hand(ctx.opponent_id)) if is_pokemon_card(c)]
    if not pokemon:
        return
    picks = await ctx.choose_cards(pokemon, 1, minimum=1, prompt="Choose a Pokémon to discard")
    if picks:
        await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="e9d64bdd-3553-5950-892f-582e6cfd3d32",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PretendPlasmaBossPikachu.Name",
    display_name="Pretend Plasma Boss Pikachu",
    searchable_by=["Pretend Plasma Boss Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=195,
    set_code="SMPJ",
    regulation_mark="B",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Liberate?",
            game_text="Look at your opponent's hand and discard a Pokémon you find there.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_liberate,
        ),
        Attack(
            title="Pika Punch",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
