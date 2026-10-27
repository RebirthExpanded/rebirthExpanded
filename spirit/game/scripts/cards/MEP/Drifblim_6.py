"""Drifblim (MEP 6 -- JP SVP 235; English MEP/6). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import full_stack


async def balloon_return(ctx):
    await ctx.deal_damage()
    if ctx.attacker not in ctx.knockouts and ctx.my_bench():
        await ctx.put_in_hand(full_stack(ctx.attacker), reveal=False)


card = PokemonCardDef(
    guid="b2e34aee-b100-53bc-ad51-cd881a486a6c",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifblim.Name",
    display_name="Drifblim",
    searchable_by=["Drifblim", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="MEP",
    regulation_mark="I",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    family_id=425,
    abilities=[
        Attack(
            title="Creepy Wind",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Balloon Return",
            game_text="Put this Pokémon and all attached cards into your hand.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=110,
            effect=balloon_return,
        ),
    ],
)
