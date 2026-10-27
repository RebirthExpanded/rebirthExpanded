"""Paras (SV09 4 -- JP SV9 004; English JTG/4). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _leech(ctx):
    dealt = await ctx.deal_damage()
    if dealt:
        await ctx.heal(dealt, ctx.attacker)


card = PokemonCardDef(
    guid="ed1b420f-a372-5d2f-9bfd-0da9fd4b1cc9",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name",
    display_name="Paras",
    searchable_by=["Paras", "Basic"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=46,
    abilities=[
        Attack(
            title="Leech Life",
            game_text="Heal from this Pokémon the same amount of damage you did to your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=_leech,
        ),
    ],
)
