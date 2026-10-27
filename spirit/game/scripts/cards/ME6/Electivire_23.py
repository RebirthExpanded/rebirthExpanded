"""Electivire (ME6 23 -- JP M6 023; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card


async def voltage_hammer(ctx):
    pool = [e for e in ctx.attached_energies(ctx.attacker) if is_basic_energy_card(e)]
    picks = []
    if pool:
        picks = await ctx.choose_cards(pool, len(pool), minimum=0, prompt="Discard any amount of Basic Energy from this Pokémon.")
        if picks:
            await ctx.discard_cards(picks)
    await ctx.deal_damage(60 * len(picks))


card = PokemonCardDef(
    guid="e47ebff9-b0a6-572c-926b-44202c01a899",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electivire.Name",
    display_name="Electivire",
    searchable_by=["Electivire", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    family_id=239,
    abilities=[
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Voltage Hammer",
            game_text="Discard any amount of Basic Energy from this Pokémon. This attack does 60 damage for each card you discarded in this way.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=voltage_hammer,
        ),
    ],
)
