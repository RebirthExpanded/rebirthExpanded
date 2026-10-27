"""Revavroom ex (SV065 15 -- JP SV6a 015; English SFA/15, SFA/81). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import full_stack


def _entered_active_this_turn(ctx) -> bool:
    return ctx.entered_active_this_turn(ctx.attacker)


async def shattering_speed(ctx):
    await ctx.deal_damage()
    if ctx.attacker not in ctx.knockouts:
        await ctx.discard_cards(full_stack(ctx.attacker))


card = PokemonCardDef(
    guid="095ad5af-cbbc-5a3b-824c-ad12545556b7",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Revavroomex.Name",
    display_name="Revavroom ex",
    searchable_by=["Revavroom ex", "Stage 1", "ex", "Tera"],
    subtypes=["Stage 1", "ex", "Tera"],
    collector_number=15,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name",
    family_id=965,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Accelerator Flash",
            game_text="If this Pokémon moved from your Bench to the Active Spot this turn, this attack does 120 more damage.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            damage_operator="+",
            effect=ac.bonus_if(_entered_active_this_turn, 120),
        ),
        Attack(
            title="Shattering Speed",
            game_text="Discard this Pokémon and all attached cards.",
            cost={PokemonTypes.METAL: 3},
            damage=250,
            effect=shattering_speed,
        ),
    ],
)
