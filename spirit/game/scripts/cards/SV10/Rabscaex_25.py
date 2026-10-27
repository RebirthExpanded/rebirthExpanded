"""Rabsca ex (SV10 25 -- JP SVP 184; English DRI/25). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def upside_down_draw(ctx):
    deck = list(ctx.deck())
    picks = deck[-3:] if deck else []
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="ee1efa9e-1e89-50ca-a33d-20b0795b7e35",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rabscaex.Name",
    display_name="Rabsca ex",
    searchable_by=["Rabsca ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=25,
    set_code="SV10",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rellor.Name",
    family_id=953,
    abilities=[
        Attack(
            title="Upside-Down Draw",
            game_text="Draw 3 cards from the bottom of your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=upside_down_draw,
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 90 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("defender"), 90, base=20),
        ),
    ],
)
