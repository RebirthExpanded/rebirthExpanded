"""Scolipede (ZSV10PT5 56 -- JP SV11B 059; English BLK/134, BLK/56). Japanese art.
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
    guid="6d6b0354-502d-53e7-baa7-eb41b3dfa8cd",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scolipede.Name",
    display_name="Scolipede",
    searchable_by=["Scolipede", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=56,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Whirlipede.Name",
    family_id=543,
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
            game_text="If your opponent's Active Pokémon is Poisoned, this attack does 90 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=ac.condition_bonus_attack(90, SpecialConditions.POISONED),
        ),
    ],
)
