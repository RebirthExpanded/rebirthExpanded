"""Mantyke (SV4 39 -- JP SV3a 007; English PAR/189, PAR/39). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def buoyant_healing(ctx):
    pool = [p for p in ctx.my_bench() if _counters(ctx.board, p) > 0]
    if pool:
        target = await ctx.choose_pokemon(pool, "Choose 1 of your Benched Pokémon to heal 120 damage from")
        if target is not None:
            await ctx.heal(120, target)


card = PokemonCardDef(
    guid="d6b2629b-e23d-50d2-8e1e-3e0250777f04",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mantyke.Name",
    display_name="Mantyke",
    searchable_by=["Mantyke", "Basic"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=458,
    abilities=[
        Attack(
            title="Buoyant Healing",
            game_text="Heal 120 damage from 1 of your Benched Pokémon.",
            cost={},
            effect=buoyant_healing,
        ),
    ],
)
