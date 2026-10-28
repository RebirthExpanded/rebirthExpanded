"""Eevee (SV3 166 -- JP SV3 091; English OBF/166). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_energy_card


async def cheer_up(ctx):
    pool = [c for c in ctx.hand() if is_energy_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Energy card to attach")
    target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon") if picks else None
    if target is not None:
        await ctx.attach_energy(picks[0], target)


card = PokemonCardDef(
    guid="1e6758c5-640c-5449-9452-5120cb1fbb8e",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic"],
    subtypes=["Basic"],
    collector_number=166,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Cheer Up",
            game_text="Attach an Energy card from your hand to 1 of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=cheer_up,
        ),
        Attack(
            title="Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
