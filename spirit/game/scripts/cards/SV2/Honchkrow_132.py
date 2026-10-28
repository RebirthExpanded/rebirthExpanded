"""Honchkrow (SV2 132 -- JP SV2P 046; English PAL/132). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def dirty_throw(ctx):
    if not ctx.hand():
        return
    paid = await ctx.discard_from_hand(1, minimum=1, prompt="Discard a card from your hand")
    if paid:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="8c7cfe5d-8766-588b-b077-d0617f99b5be",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Honchkrow.Name",
    display_name="Honchkrow",
    searchable_by=["Honchkrow", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=132,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    family_id=198,
    abilities=[
        Attack(
            title="Flap",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
        ),
        Attack(
            title="Dirty Throw",
            game_text="Discard a card from your hand. If you can't, this attack does nothing.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=dirty_throw,
        ),
    ],
)
