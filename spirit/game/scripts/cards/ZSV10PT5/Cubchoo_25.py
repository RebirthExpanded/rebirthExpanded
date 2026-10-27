"""Cubchoo (ZSV10PT5 25 -- JP SV11B 028; English BLK/109, BLK/25). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock_defender(ctx):
    await ctx.deal_damage()
    ac.lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="8c72a1ee-ad6f-5b7c-98a0-1d39a90a576c",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cubchoo.Name",
    display_name="Cubchoo",
    searchable_by=["Cubchoo", "Basic"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=613,
    abilities=[
        Attack(
            title="Snotted Up",
            game_text="During your opponent's next turn, the Defending Pokémon can't use attacks.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=_hit_then_lock_defender,
        ),
    ],
)
