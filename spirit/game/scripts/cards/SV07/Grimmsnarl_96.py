"""Grimmsnarl (SV07 96 -- JP SV7 066; English SCR/96). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


async def goad_n_grab(ctx):
    old = ctx.opponent_active()
    if old is None or ctx.effects_blocked(old):
        return
    new = await su.opponent_switches(ctx)
    if new is not None:
        await ctx.deal_damage(160, target=new)


card = PokemonCardDef(
    guid="7a658b26-4db2-5b75-a15d-dde0231042ae",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grimmsnarl.Name",
    display_name="Grimmsnarl",
    searchable_by=["Grimmsnarl", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=96,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Morgrem.Name",
    family_id=859,
    abilities=[
        Attack(
            title="Goad 'n' Grab",
            game_text="Switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.) If you do, this attack does 160 damage to the new Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=goad_n_grab,
        ),
        Attack(
            title="Knuckle Sandwich",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=ac.self_energy_discard_attack(count=2),
        ),
    ],
)
