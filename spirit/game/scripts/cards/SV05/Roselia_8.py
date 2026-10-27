"""Roselia (SV05 8 -- JP SV5K 001; English TEF/8). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import passives_common as pc


async def _poison_attacker(ctx):
    attacker = ctx.damaged_by
    if attacker is not None:
        await ctx.apply_special_condition(attacker, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="8ac193b3-ab32-5bd7-ba5c-c6152fa60e79",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name",
    display_name="Roselia",
    searchable_by=["Roselia", "Basic"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=406,
    abilities=[
        Ability(
            title="Poison Point",
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Poisoned.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=pc.hit_in_active_by_opponent,
            effect=_poison_attacker,
        ),
        Attack(
            title="Leaf Step",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
