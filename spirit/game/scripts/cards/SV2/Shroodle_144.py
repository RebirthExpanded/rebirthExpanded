"""Shroodle (SV2 144 -- JP SV2D 053; English PAF/189, PAL/144). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card


async def berry_search(ctx):
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if pool:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Energy card")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="471b87c5-9a4c-5b1d-94ef-63c5d5b5e44c",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shroodle.Name",
    display_name="Shroodle",
    searchable_by=["Shroodle", "Basic"],
    subtypes=["Basic"],
    collector_number=144,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=944,
    abilities=[
        Attack(
            title="Berry Search",
            game_text="Put a Basic Energy card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=berry_search,
        ),
        Attack(
            title="Scratch",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)
