"""Magnezone ex (SV1 65 -- JP SV1V 028; English SVI/226, SVI/65). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def energy_crush(ctx):
    n = sum(len(ctx.attached_energies(p)) for p in ctx.opponent_pokemon_in_play())
    if n:
        await ctx.deal_damage(50 * n)


card = PokemonCardDef(
    guid="4f1f50d8-b2f2-5b4f-b5d3-4ca20269b06f",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnezoneex.Name",
    display_name="Magnezone ex",
    searchable_by=["Magnezone ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=65,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    family_id=81,
    abilities=[
        Attack(
            title="Energy Crush",
            game_text="This attack does 50 damage for each Energy attached to all of your opponent's Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=50,
            damage_operator="x",
            effect=energy_crush,
        ),
        Attack(
            title="Pulse Launcher",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=220,
            effect=ac.recoil_attack(30),
        ),
    ],
)
