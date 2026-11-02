"""Pikachu (SMPJ 224 -- JP SMP 224; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _celebrate_together(ctx):
    """Heal 20 damage from each Pokemon (both yours and your opponent's)."""
    for pokemon in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
        await ctx.heal(20, pokemon)


card = PokemonCardDef(
    guid="024c1877-6230-53ef-8be1-160bd48f508c",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=224,
    set_code="SMPJ",
    regulation_mark="B",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Celebrate Together",
            game_text="Heal 20 damage from each Pokémon (both yours and your opponent's).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_celebrate_together,
        ),
        Attack(
            title="Tail Whap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
