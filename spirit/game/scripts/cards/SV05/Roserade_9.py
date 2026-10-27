"""Roserade (SV05 9 -- JP SV5K 002; English TEF/9). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import passives_common as pc


async def _poison_attacker(ctx):
    attacker = ctx.damaged_by
    if attacker is not None:
        await ctx.apply_special_condition(attacker, SpecialConditions.POISONED)
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="4b470f80-eccc-58b3-a187-aca0b39521ee",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roserade.Name",
    display_name="Roserade",
    searchable_by=["Roserade", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name",
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
            title="Bind Down",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=ac.condition_attack(no_retreat=True),
        ),
    ],
)
