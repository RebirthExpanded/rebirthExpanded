"""Magcargo ex (SV06 29 -- JP SV5a 013; English TWM/191, TWM/29). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_energy_card


async def ground_burn(ctx):
    top = []
    for pid in (ctx.player_id, ctx.opponent_id):
        top += list(ctx.deck_top(1, player_id=pid))
    if top:
        await ctx.discard_cards(top)
    n = sum(1 for c in top if is_energy_card(c))
    await ctx.deal_damage(140 + 140 * n)


card = PokemonCardDef(
    guid="3156720b-f0ae-5d75-9a95-199bc0dbf263",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magcargoex.Name",
    display_name="Magcargo ex",
    searchable_by=["Magcargo ex", "Stage 1", "ex", "Tera"],
    subtypes=["Stage 1", "ex", "Tera"],
    collector_number=29,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    family_id=218,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Hot Magma",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=ac.condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Ground Burn",
            game_text="Discard the top card of each player's deck. This attack does 140 more damage for each Energy card discarded in this way.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
            damage_operator="+",
            effect=ground_burn,
        ),
    ],
)
