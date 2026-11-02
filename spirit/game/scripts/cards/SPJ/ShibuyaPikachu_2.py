"""Shibuya Pikachu (SPJ 2 -- JP SP 002; English Japan only). Japanese art.
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
    guid="9cd1d186-a984-5405-982d-c3c0a6637ae5",
    key="SPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShibuyaPikachu.Name",
    display_name="Shibuya Pikachu",
    searchable_by=["Shibuya Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=2,
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
            title="Thunder",
            game_text="Flip a coin. If tails, this Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=ac.flip_damage(coins=1, tails_self_damage=20),
        ),
    ],
)
