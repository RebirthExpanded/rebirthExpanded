"""Qwilfish (ME4 52 -- JP M4 051; English CRI/52). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import SpecialConditions

from spirit.game.card_effects.passives_common import hit_in_active_by_opponent


async def _poison_point(ctx):
    """Active Spot only: damaged by an opponent's attack (even if Knocked
    Out), the Attacking Pokemon is now Poisoned."""
    attacker = ctx.damaged_by
    if attacker is not None:
        await ctx.apply_special_condition(attacker, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="72204183-ecd8-5e99-b90b-10813b1c0baa",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Qwilfish.Name",
    display_name="Qwilfish",
    searchable_by=["Qwilfish", "Basic"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=211,
    abilities=[
        Ability(
            title="Poison Point",
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Poisoned.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=hit_in_active_by_opponent,
            effect=_poison_point,
        ),
        Attack(
            title="Venoshock",
            game_text="If your opponent's Active Pokémon is Poisoned, this attack does 50 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            damage_operator="+",
            effect=ac.condition_bonus_attack(50, SpecialConditions.POISONED),
        ),
    ],
)
