"""Thievul (ME1 90 -- JP M1L 042; English MEG/90). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def greedy_hunt(ctx):
    await ctx.deal_damage()
    if len(ctx.hand()) < 6 and await ctx.ask_yes_no("Draw cards until you have 6 cards in your hand?"):
        await ctx.draw_until(6)


card = PokemonCardDef(
    guid="00e79ad7-2bdc-556e-aa3d-47d172892c9d",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thievul.Name",
    display_name="Thievul",
    searchable_by=["Thievul", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=90,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nickit.Name",
    family_id=827,
    abilities=[
        Attack(
            title="Greedy Hunt",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=greedy_hunt,
        ),
        Attack(
            title="Pitch-Black Fangs",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
