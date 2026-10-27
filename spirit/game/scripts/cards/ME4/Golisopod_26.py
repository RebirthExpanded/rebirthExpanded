"""Golisopod (ME4 26 -- JP M4 026; English CRI/26). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


async def critical_slash(ctx):
    defender = ctx.defender
    await ctx.deal_damage()
    if defender is not None and defender in ctx.knockouts:
        await pc.apply_protection(ctx, prevent=True, effects_too=True)


card = PokemonCardDef(
    guid="1f7c307c-c868-5b4f-bea1-4a24b01edbfb",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golisopod.Name",
    display_name="Golisopod",
    searchable_by=["Golisopod", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    family_id=767,
    abilities=[
        Attack(
            title="Critical Slash",
            game_text="If your opponent's Pokémon is Knocked Out by damage from this attack, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=critical_slash,
        ),
        Attack(
            title="Boundless Power",
            game_text="During your next turn, this Pokémon can't use attacks.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=_hit_then_lock,
        ),
    ],
)
