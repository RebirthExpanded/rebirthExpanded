"""Pikachu (XYPJ 279 -- JP XYP 279; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

_discard_all = ac.self_energy_discard_attack(all_energy=True)



async def _party(ctx):
    await ctx.draw_cards(1)
    await ctx.draw_cards(1, player_id=ctx.opponent_id)


card = PokemonCardDef(
    guid="3d89df98-fc81-51c1-90d5-0e55b1760dad",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=279,
    set_code="XYPJ",
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
            title="Celebration Party!",
            game_text="Both players clap! Then, each player draws a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_party,
        ),
        Attack(
            title="1,000,000 Volts",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 4},
            damage=120,
            effect=_discard_all,
        ),
    ],
)
