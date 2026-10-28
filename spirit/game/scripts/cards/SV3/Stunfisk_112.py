"""Stunfisk (SV3 112 -- JP SV3 059; English OBF/112). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc


def _revenge(n):
    async def effect(ctx):
        attacker = ctx.damaged_by
        if attacker is not None:
            await ctx.deal_damage(10 * n, target=attacker, apply_modifiers=False, as_counters=True, is_attack=False)
    return effect



def _custom_trap_applies(ctx) -> bool:
    return pc.hit_in_active_by_opponent(ctx) and ac.has_tool(ctx.source)


card = PokemonCardDef(
    guid="060d66af-a603-5689-80f0-26ea3a2eea2f",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stunfisk.Name",
    display_name="Stunfisk",
    searchable_by=["Stunfisk", "Basic"],
    subtypes=["Basic"],
    collector_number=112,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=618,
    abilities=[
        Ability(
            title="Custom Trap",
            game_text="If this Pokémon is in the Active Spot, has a Pokémon Tool attached, and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), put 5 damage counters on the Attacking Pokémon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=_custom_trap_applies,
            effect=_revenge(5),
        ),
        Attack(
            title="Rumble",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=ac.condition_attack(no_retreat=True),
        ),
    ],
)
