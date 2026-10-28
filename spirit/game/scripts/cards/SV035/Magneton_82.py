"""Magneton (SV035 82 -- JP SV2a 082; English MEW/82). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_item_card


async def junk_magnet(ctx):
    pool = [c for c in ctx.discard_pile() if is_item_card(c)]
    if pool:
        picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Choose up to 2 Item cards")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="72ed23ff-016c-5870-b39a-f2c32c3f0cf5",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    display_name="Magneton",
    searchable_by=["Magneton", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    family_id=81,
    abilities=[
        Attack(
            title="Junk Magnet",
            game_text="Put up to 2 Item cards from your discard pile into your hand.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=junk_magnet,
        ),
        Attack(
            title="Head Bolt",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
