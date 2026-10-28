"""Alomomola (SV1 48 -- JP SVAW 001; English SVI/48). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="13f36902-14f3-5d13-bf0e-d2a0d33033e9",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alomomola.Name",
    display_name="Alomomola",
    searchable_by=["Alomomola", "Basic"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=594,
    abilities=[
        Attack(
            title="Surf",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Aqua Slash",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=_hit_then_lock,
        ),
    ],
)
