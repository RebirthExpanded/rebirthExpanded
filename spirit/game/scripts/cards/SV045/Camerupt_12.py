"""Camerupt (SV045 12 -- JP SV4K 012; English PAF/12). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


async def cinder_cannon(ctx):
    pool = [e for e in ctx.attached_energies(ctx.attacker) if is_energy_of_type(e, PokemonTypes.FIGHTING)]
    if pool and await ctx.ask_yes_no("Discard a Fighting Energy from this Pokémon for 120 more damage?"):
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Fighting Energy to discard")
        await ctx.discard_cards(picks)
        await ctx.deal_damage(240)
    else:
        await ctx.deal_damage(120)


card = PokemonCardDef(
    guid="9a54e06e-2188-5048-bb8e-1e08f3d59d48",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Camerupt.Name",
    display_name="Camerupt",
    searchable_by=["Camerupt", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name",
    family_id=322,
    abilities=[
        Attack(
            title="Super Singe",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=ac.condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Cinder Cannon",
            game_text="You may discard a Fighting Energy from this Pokémon. If you do, this attack does 120 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=cinder_cannon,
        ),
    ],
)
