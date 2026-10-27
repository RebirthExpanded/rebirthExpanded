"""Sunflora (SV06 7 -- JP SV6 002; English TWM/169, TWM/7). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


async def redirected_sunlight(ctx):
    n = sum(1 for p in ctx.opponent_pokemon_in_play() for e in ctx.attached_energies(p)
            if is_energy_of_type(e, PokemonTypes.FIRE))
    if n:
        await ctx.deal_damage(60 * n)


card = PokemonCardDef(
    guid="90f922d1-eb85-5672-a129-d6b83d8829f2",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sunflora.Name",
    display_name="Sunflora",
    searchable_by=["Sunflora", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sunkern.Name",
    family_id=191,
    abilities=[
        Attack(
            title="Redirected Sunlight",
            game_text="This attack does 60 damage for each Fire Energy attached to all of your opponent's Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            damage_operator="x",
            effect=redirected_sunlight,
        ),
        Attack(
            title="Mega Drain",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=su.heal_attack(30),
        ),
    ],
)
