"""Erika's Weepinbell (ME2PT5 5 -- JP MC 007; English ASC/5). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="e4beed73-e2d7-5374-adcf-7ce9a7c63049",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasWeepinbell.Name",
    display_name="Erika's Weepinbell",
    searchable_by=["Erika's Weepinbell", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasBellsprout.Name",
    family_id=69,
    abilities=[
        Attack(
            title="Melt",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
        Attack(
            title="Leafy Cyclone",
            game_text="During your next turn, this Pokémon can't use attacks.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=_hit_then_lock,
        ),
    ],
)
