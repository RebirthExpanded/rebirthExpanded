"""Comedy Pikachu (SMPJ 407 -- JP SMP 407; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac



async def _new_open(ctx):
    """Each player reveals the top card of their deck and puts it into their hand."""
    tops = [c for pid in (ctx.player_id, ctx.opponent_id) for c in ctx.deck_top(1, player_id=pid)]
    if tops:
        await ctx.put_in_hand(tops, reveal=True)


card = PokemonCardDef(
    guid="1b4c624c-ed40-55d7-a1c7-8c5cebcd563e",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ComedyPikachu.Name",
    display_name="Comedy Pikachu",
    searchable_by=["Comedy Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=407,
    set_code="SMPJ",
    regulation_mark="C",
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
            title="New Open",
            game_text="Each player reveals the top card of their deck and puts it into their hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_new_open,
        ),
        Attack(
            title="Whimsy Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
