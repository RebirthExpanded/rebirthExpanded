"""Cacnea (SV1 5 -- JP SV1S 001; English SVI/5). Japanese art.
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
    guid="f41b4a5c-ef13-54b3-8dd2-b61a81449c2e",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name",
    display_name="Cacnea",
    searchable_by=["Cacnea", "Basic"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
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
            title="Light Punch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
