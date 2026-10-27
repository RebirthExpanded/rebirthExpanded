"""Octillery (ME4 17 -- JP M4 017; English CRI/17). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


async def jet_of_ink(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        ctx.require_attack_flip(defender, coins=2)


async def tantrum(ctx):
    await ctx.deal_damage()
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="591b9ee8-3052-54d5-ae1b-9105228cea71",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Octillery.Name",
    display_name="Octillery",
    searchable_by=["Octillery", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    family_id=223,
    abilities=[
        Attack(
            title="Jet of Ink",
            game_text="During your opponent's next turn, if the Defending Pokémon tries to use an attack, your opponent flips 2 coins. If either of them is tails, that attack doesn't happen.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=jet_of_ink,
        ),
        Attack(
            title="Tantrum",
            game_text="This Pokémon is now Confused.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=tantrum,
        ),
    ],
)
