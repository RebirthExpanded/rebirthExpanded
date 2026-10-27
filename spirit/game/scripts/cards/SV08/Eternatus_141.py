"""Eternatus (SV08 141 -- JP SV8 080; English SSP/141). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _defender_ex(ctx) -> bool:
    return ctx.defender is not None and "ex" in (subtypes_for(ctx.defender.archetype_id) or [])


async def world_ender(ctx):
    if ctx.stadium_in_play() is None:
        return
    await ctx.discard_stadium()
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="e1bd9e4c-491a-5a6e-9efd-545af7b135cd",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eternatus.Name",
    display_name="Eternatus",
    searchable_by=["Eternatus", "Basic"],
    subtypes=["Basic"],
    collector_number=141,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=890,
    abilities=[
        Attack(
            title="Dyna-Blast",
            game_text="If your opponent's Active Pokémon is a Pokémon ex, this attack does 80 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            damage_operator="+",
            effect=ac.bonus_if(_defender_ex, 80),
        ),
        Attack(
            title="World Ender",
            game_text="Discard a Stadium in play. If you can't, this attack does nothing.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.DARKNESS: 2},
            damage=230,
            effect=world_ender,
        ),
    ],
)
