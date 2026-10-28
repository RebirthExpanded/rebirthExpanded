"""Donphan (SV045 49 -- JP SV3a 025; English PAF/49). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="e356cda2-a507-56e9-8c05-6ad2fcc3db34",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Donphan.Name",
    display_name="Donphan",
    searchable_by=["Donphan", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name",
    family_id=231,
    abilities=[
        Attack(
            title="Cragalanche",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=ac.mill_attack(2),
        ),
        Attack(
            title="Powerful Spin",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=_hit_then_lock,
        ),
    ],
)
