"""Rillaboom (SV06 16 -- JP SV6 010; English TWM/16). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac


async def drum_beating(ctx):
    await ctx.deal_damage()
    await pc.apply_defender_attack_cost_raise(ctx, 1)
    await pc.apply_defender_retreat_cost_raise(ctx, 1)


card = PokemonCardDef(
    guid="c702429c-37ed-5492-ba72-a3a09b5959a0",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rillaboom.Name",
    display_name="Rillaboom",
    searchable_by=["Rillaboom", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=16,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Thwackey.Name",
    family_id=810,
    abilities=[
        Attack(
            title="Drum Beating",
            game_text="During your opponent's next turn, attacks used by the Defending Pokémon cost Colorless more, and its Retreat Cost is Colorless more.",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            effect=drum_beating,
        ),
        Attack(
            title="Wood Hammer",
            game_text="This Pokémon also does 50 damage to itself.",
            cost={PokemonTypes.GRASS: 2},
            damage=180,
            effect=ac.recoil_attack(50),
        ),
    ],
)
