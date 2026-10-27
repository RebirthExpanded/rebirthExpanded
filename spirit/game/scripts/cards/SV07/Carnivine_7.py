"""Carnivine (SV07 7 -- JP SV7 005; English SCR/7). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def loom_over(ctx):
    amount = max(0, 130 - 10 * _counters(ctx.board, ctx.attacker))
    if amount:
        await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid="e454496b-7ef2-5419-9916-68c69353da1f",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carnivine.Name",
    display_name="Carnivine",
    searchable_by=["Carnivine", "Basic"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=455,
    abilities=[
        Attack(
            title="Nosh",
            game_text="Heal 40 damage from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.heal_attack(40),
        ),
        Attack(
            title="Loom Over",
            game_text="This attack does 10 less damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            damage_operator="-",
            effect=loom_over,
        ),
    ],
)
