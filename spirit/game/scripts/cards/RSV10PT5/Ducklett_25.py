"""Ducklett (RSV10PT5 25 -- JP SV11W 022; English WHT/109, WHT/25). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


async def firefighting(ctx):
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    pool = [e for e in ctx.attached_energies(target) if is_energy_of_type(e, PokemonTypes.FIRE)]
    if pool:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Fire Energy to discard")
        await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="fe3f48af-078c-5076-b711-efee813e4c8c",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ducklett.Name",
    display_name="Ducklett",
    searchable_by=["Ducklett", "Basic"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=580,
    abilities=[
        Attack(
            title="Firefighting",
            game_text="Discard a Fire Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=firefighting,
        ),
        Attack(
            title="Wing Attack",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
