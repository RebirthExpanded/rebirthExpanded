"""Kanazawa's Pikachu (SPJ 144 -- JP SP 144; English Japan only). Japanese art.
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
    guid="6f75ca7f-4ad1-549c-b73b-1ce5e4338b98",
    key="SPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KanazawasPikachu.Name",
    display_name="Kanazawa's Pikachu",
    searchable_by=["Kanazawa's Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=144,
    set_code="SPJ",
    regulation_mark="D",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="New Open",
            game_text="Each player reveals the top card of their deck and puts it into their hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_new_open,
        ),
        Attack(
            title="Pika Walk",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=ac.flip_bonus(30),
        ),
    ],
)
