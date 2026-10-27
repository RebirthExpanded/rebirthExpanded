"""Komala (SV09 129 -- JP SV9 082; English JTG/129). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import passives_common as pc


async def slumbering_smack(ctx):
    await ctx.deal_damage()
    for target in (ctx.opponent_active(), ctx.attacker):
        if target is not None and target not in ctx.knockouts:
            await ctx.apply_special_condition(target, SpecialConditions.ASLEEP)
    await pc.boost_own_next_turn(100)(_NoDamage(ctx))


class _NoDamage:
    """Runs boost_own_next_turn's rider without its printed damage."""

    def __init__(self, ctx):
        self._ctx = ctx

    def __getattr__(self, name):
        return getattr(self._ctx, name)

    async def deal_damage(self, *a, **k):
        return 0


card = PokemonCardDef(
    guid="370e0f07-af3f-59c5-8177-0ba599b84706",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Komala.Name",
    display_name="Komala",
    searchable_by=["Komala", "Basic"],
    subtypes=["Basic"],
    collector_number=129,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=775,
    abilities=[
        Attack(
            title="Slumbering Smack",
            game_text="Both Active Pokémon are now Asleep. During your next turn, attacks used by this Pokémon do 100 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=slumbering_smack,
        ),
    ],
)
