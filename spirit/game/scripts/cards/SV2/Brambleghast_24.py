"""Brambleghast (SV2 24 -- JP SV2P 012; English PAL/24). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import passives_common as pc


async def dead_wood_detention(ctx):
    await ctx.deal_damage()
    await pc.apply_defender_attack_cost_raise(ctx, 2)


card = PokemonCardDef(
    guid="f2e9b15e-7a8f-592e-945e-277b1e1a1bf4",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Brambleghast.Name",
    display_name="Brambleghast",
    searchable_by=["Brambleghast", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bramblin.Name",
    family_id=946,
    abilities=[
        Attack(
            title="Absorb Life",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=su.heal_attack(30),
        ),
        Attack(
            title="Dead Wood Detention",
            game_text="During your opponent's next turn, attacks that the Defending Pokémon uses cost ColorlessColorless more.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=dead_wood_detention,
        ),
    ],
)
