"""Ceruledge (SV08 35 -- JP SV8 022; English SSP/197, SSP/35). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)

from spirit.game.session.effects import is_special_energy


async def cursed_edge(ctx):
    junk = [e for p in ctx.opponent_pokemon_in_play() if not ctx.effects_blocked(p)
            for e in ctx.attached_energies(p) if is_special_energy(e)]
    if junk:
        await ctx.discard_cards(junk)


card = PokemonCardDef(
    guid="a9f91289-60ee-55ff-872a-9a02600ca910",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ceruledge.Name",
    display_name="Ceruledge",
    searchable_by=["Ceruledge", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    family_id=935,
    abilities=[
        Attack(
            title="Cursed Edge",
            game_text="Discard all Special Energy from all of your opponent's Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=cursed_edge,
        ),
        Attack(
            title="Black Blaze Slash",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=_hit_then_lock,
        ),
    ],
)
