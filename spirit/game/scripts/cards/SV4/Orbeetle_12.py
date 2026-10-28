"""Orbeetle (SV4 12 -- JP SV4M 005; English PAR/12). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_energy_card


async def satellite_beam(ctx):
    n = sum(1 for c in ctx.discard_pile(ctx.opponent_id) if is_energy_card(c))
    if n:
        await ctx.deal_damage(30 * n)


card = PokemonCardDef(
    guid="71702f05-fca7-5949-be31-5baf7bc566a7",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Orbeetle.Name",
    display_name="Orbeetle",
    searchable_by=["Orbeetle", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=12,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dottler.Name",
    family_id=824,
    abilities=[
        Attack(
            title="Satellite Beam",
            game_text="This attack does 30 damage for each Energy card in your opponent's discard pile.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator="x",
            effect=satellite_beam,
        ),
        Attack(
            title="Brain Shake",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
