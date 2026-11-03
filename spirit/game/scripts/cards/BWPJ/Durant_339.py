"""Durant (BWPJ 339 -- JP WAK 039; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac



async def _crunch(ctx):
    """Printed damage, then flip a coin: heads discards an Energy from the opponent's Active."""
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "")
    if results and results[0]:
        await ac.discard_opponent_energy_attack(1)(ctx)
    else:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="6b211ae1-9e48-5046-8a28-5663ef3794cf",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Durant.Name",
    display_name="Durant",
    searchable_by=["Durant", "Basic"],
    subtypes=["Basic"],
    collector_number=339,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=632,
    abilities=[
        Attack(
            title="Vise Grip",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=_crunch,
        ),
    ],
)
