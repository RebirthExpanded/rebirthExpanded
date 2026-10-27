"""Beautifly (ME2PT5 13 -- JP M2a 006; English ASC/13, ASC/219). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_energy_card


async def energy_straw(ctx):
    hand = list(ctx.hand(ctx.opponent_id))
    if hand:
        await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    n = sum(1 for c in hand if is_energy_card(c))
    if n:
        await ctx.deal_damage(80 * n)


card = PokemonCardDef(
    guid="a19195af-de7e-5478-bfd1-52013026507f",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beautifly.Name",
    display_name="Beautifly",
    searchable_by=["Beautifly", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Silcoon.Name",
    family_id=265,
    abilities=[
        Attack(
            title="Stun Spore",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=40,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Energy Straw",
            game_text="Your opponent reveals their hand, and this attack does 80 damage for each Energy card you find there.",
            cost={PokemonTypes.GRASS: 1},
            damage=80,
            damage_operator="x",
            effect=energy_straw,
        ),
    ],
)
