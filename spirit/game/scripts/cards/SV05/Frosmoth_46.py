"""Frosmoth (SV05 46 -- JP SV5K 020; English TEF/46). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock_defender(ctx):
    await ctx.deal_damage()
    ac.lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="db9e067a-73b5-5c25-9524-c9d18f7a701b",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Frosmoth.Name",
    display_name="Frosmoth",
    searchable_by=["Frosmoth", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snom.Name",
    family_id=872,
    abilities=[
        Attack(
            title="Freezing Chill",
            game_text="During your opponent's next turn, the Defending Pokémon can't attack.",
            cost={PokemonTypes.WATER: 2},
            damage=100,
            effect=_hit_then_lock_defender,
        ),
    ],
)
