"""Cryogonal (SV3 55 -- JP SV3 028; English OBF/55). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


async def first_freeze(ctx):
    await ctx.deal_damage()
    going_second = ctx.player_id != ctx.session.first_player_id
    d = ctx.opponent_active()
    if going_second and ctx.session.turn_state.turn_number == 2 and d is not None and d not in ctx.knockouts:
        await ctx.apply_special_condition(d, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="6ffd52c9-fe8a-5b5e-9f76-cc5a9e1e6f3c",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cryogonal.Name",
    display_name="Cryogonal",
    searchable_by=["Cryogonal", "Basic"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=615,
    abilities=[
        Attack(
            title="First Freeze",
            game_text="If you go second and it's your first turn, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=first_freeze,
        ),
    ],
)
