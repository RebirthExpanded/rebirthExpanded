"""Armarouge (SV3 44 -- JP SVD 021; English OBF/44). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import passives_common as pc


async def _burn_attacker(ctx):
    attacker = ctx.damaged_by
    if attacker is not None:
        await ctx.apply_special_condition(attacker, SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="8611900a-5130-57cd-871a-4f88e24e1447",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Armarouge.Name",
    display_name="Armarouge",
    searchable_by=["Armarouge", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    family_id=935,
    abilities=[
        Ability(
            title="Scorching Armor",
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Burned.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=pc.hit_in_active_by_opponent,
            effect=_burn_attacker,
        ),
        Attack(
            title="Steam Artillery",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
