"""Klawf (SV1 122 -- JP SV1S 048; English SVI/122, SVI/217). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


async def adrenaline_hammer(ctx):
    await ctx.deal_damage()
    if ctx.attacker not in ctx.knockouts:
        await ctx.apply_special_condition(ctx.attacker, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="0f6adf46-1cbf-5eee-81d2-f4be5641d75c",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klawf.Name",
    display_name="Klawf",
    searchable_by=["Klawf", "Basic"],
    subtypes=["Basic"],
    collector_number=122,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=950,
    abilities=[
        Attack(
            title="Vise Grip",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
        ),
        Attack(
            title="Adrenaline Hammer",
            game_text="This Pokémon is now Confused.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=130,
            effect=adrenaline_hammer,
        ),
    ],
)
