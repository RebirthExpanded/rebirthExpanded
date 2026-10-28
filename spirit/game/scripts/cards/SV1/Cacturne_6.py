"""Cacturne (SV1 6 -- JP SV1S 002; English SVI/6). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


def _revenge(n):
    async def effect(ctx):
        attacker = ctx.damaged_by
        if attacker is not None:
            await ctx.deal_damage(10 * n, target=attacker, apply_modifiers=False, as_counters=True, is_attack=False)
    return effect


card = PokemonCardDef(
    guid="dd2729bf-5ab4-54a6-81ca-fd5e737f319c",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cacturne.Name",
    display_name="Cacturne",
    searchable_by=["Cacturne", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name",
    family_id=331,
    abilities=[
        Ability(
            title="Counterattack Quills",
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), put 3 damage counters on the Attacking Pokémon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=pc.hit_in_active_by_opponent,
            effect=_revenge(3),
        ),
        Attack(
            title="Spike Shot",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=110,
        ),
    ],
)
