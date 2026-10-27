"""Numel (ME2PT5 27 -- JP M2a 022; English ASC/223, ASC/27). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import passives_common as pc


async def incandescent_body(ctx):
    attacker = ctx.damaged_by
    if attacker is not None:
        await ctx.apply_special_condition(attacker, SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="6fa54fb3-a81d-577b-a89b-3541f5266c5a",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name",
    display_name="Numel",
    searchable_by=["Numel", "Basic"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=322,
    abilities=[
        Ability(
            title="Incandescent Body",
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Burned.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=pc.hit_in_active_by_opponent,
            effect=incandescent_body,
        ),
        Attack(
            title="Combustion",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
