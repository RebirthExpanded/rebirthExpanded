"""Tinkatink (SV2 101 -- JP SV2D 032; English PAF/165, PAL/101, PAL/216). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_item_card


async def scrap_pickup(ctx):
    pool = [c for c in ctx.discard_pile() if is_item_card(c)]
    if pool:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Item card")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="4d359dcf-34f6-5bbf-a847-8a5638a876ab",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatink.Name",
    display_name="Tinkatink",
    searchable_by=["Tinkatink", "Basic"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=957,
    abilities=[
        Attack(
            title="Scrap Pickup",
            game_text="Put an Item card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=scrap_pickup,
        ),
        Attack(
            title="Fairy Wind",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
