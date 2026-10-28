"""Hitmonchan (SV035 107 -- JP SV2a 107; English MEW/107). Japanese art.
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
from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="110c3274-5cbc-575e-9b6e-f5218a1fa615",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonchan.Name",
    display_name="Hitmonchan",
    searchable_by=["Hitmonchan", "Basic"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=236,
    abilities=[
        Ability(
            title="Counterattack",
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), put 3 damage counters on the Attacking Pokémon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=pc.hit_in_active_by_opponent,
            effect=_revenge(3),
        ),
        Attack(
            title="Excited Punch",
            game_text="During your next turn, this Pokémon's Excited Punch attack does 60 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
            effect=pc.boost_own_next_turn(60, "Excited Punch"),
        ),
    ],
)
