"""Lycanroc (ME6A 71 -- JP M6a 071; English 30C/138, 30C/85). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def counter(ctx):
    await ctx.deal_damage(10 + ctx.damage_taken_last_turn(ctx.attacker))


card = PokemonCardDef(
    guid="ce313618-1646-5ce3-9170-2e8499fb3118",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lycanroc.Name",
    display_name="Lycanroc",
    searchable_by=["Lycanroc", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    family_id=744,
    abilities=[
        Attack(
            title="Counter",
            game_text="If this Pokémon was damaged by an attack during your opponent's last turn, this attack does that much more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="+",
            effect=counter,
        ),
        Attack(
            title="Boulder Crush",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2},
            damage=80,
        ),
    ],
)
