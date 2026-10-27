"""Stonjourner (ME1 81 -- JP M1L 033; English MEG/81). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="4446f42c-3ee0-5bf2-ae0e-25cd9dfbf1e0",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stonjourner.Name",
    display_name="Stonjourner",
    searchable_by=["Stonjourner", "Basic"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=874,
    abilities=[
        Attack(
            title="Stony Kick",
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=ac.snipe_attack(20, pool="bench", also_base=True),
        ),
        Attack(
            title="Boundless Power",
            game_text="During your next turn, this Pokémon can't use attacks.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
            effect=_hit_then_lock,
        ),
    ],
)
