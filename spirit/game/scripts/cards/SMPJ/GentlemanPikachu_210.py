"""Gentleman Pikachu (SMPJ 210 -- JP SMP 210; English Japan only). Japanese art.
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
    guid="8d734d2b-b6ec-5c9d-b737-e7ad73003043",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GentlemanPikachu.Name",
    display_name="Gentleman Pikachu",
    searchable_by=["Gentleman Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=210,
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
            title="New Open",
            game_text="Each player reveals the top card of their deck and puts it into their hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_new_open,
        ),
        Attack(
            title="Pika Cane",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=ac.flip_bonus(30),
        ),
    ],
)
