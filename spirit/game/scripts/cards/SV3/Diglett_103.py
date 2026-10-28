"""Diglett (SV3 103 -- JP SV1a 044; English OBF/103). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def hole_diggin_noggin(ctx):
    await ctx.deal_damage()
    top = list(ctx.deck_top(1))
    if top:
        await ctx.discard_cards(top)


card = PokemonCardDef(
    guid="42043a4b-1814-5afe-a308-a042261ba4f8",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name",
    display_name="Diglett",
    searchable_by=["Diglett", "Basic"],
    subtypes=["Basic"],
    collector_number=103,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=50,
    abilities=[
        Attack(
            title="Hole-Diggin' Noggin",
            game_text="Discard the top card of your deck.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=hole_diggin_noggin,
        ),
    ],
)
