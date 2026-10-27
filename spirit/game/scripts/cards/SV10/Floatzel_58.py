"""Floatzel (SV10 58 -- JP SV9a 031; English DRI/58). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="3c922a29-3c8c-55ba-8a5d-e22cf23cd539",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Floatzel.Name",
    display_name="Floatzel",
    searchable_by=["Floatzel", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name",
    family_id=418,
    abilities=[
        Attack(
            title="Whirlpool",
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=ac.discard_opponent_energy_attack(1),
        ),
        Attack(
            title="Aqua Slash",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=_hit_then_lock,
        ),
    ],
)
