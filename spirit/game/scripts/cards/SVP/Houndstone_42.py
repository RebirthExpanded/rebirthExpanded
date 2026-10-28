"""Houndstone (SVP 42 -- JP SVP 026; English SVP/42). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_item_card


async def delve(ctx):
    pool = [c for c in ctx.discard_pile() if is_item_card(c)]
    if pool:
        picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Choose up to 2 Item cards")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="04ec15a8-780f-5335-83b9-2fd232bbd311",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndstone.Name",
    display_name="Houndstone",
    searchable_by=["Houndstone", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name",
    family_id=971,
    abilities=[
        Attack(
            title="Delve",
            game_text="Put up to 2 Item cards from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=delve,
        ),
        Attack(
            title="Spooky Shot",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
