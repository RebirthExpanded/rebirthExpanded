"""Mega Tokyo's Pikachu (XYPJ 98 -- JP XYP 098; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac



async def _mega_open(ctx):
    """Both players reveal their hands to each other."""
    await ctx.reveal_hand(of_player=ctx.player_id, to_player=ctx.opponent_id)
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)


card = PokemonCardDef(
    guid="b91b70c6-830d-54ec-a5fa-5f36b11832e4",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaTokyosPikachu.Name",
    display_name="Mega Tokyo's Pikachu",
    searchable_by=["Mega Tokyo's Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Mega Open!",
            game_text="Each player reveals their hand to their opponent.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=_mega_open,
        ),
        Attack(
            title="Thunder Shock",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
