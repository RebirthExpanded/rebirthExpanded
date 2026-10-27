"""Gholdengo (SV08 131 -- JP SV7a 038; English SSP/131). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _evolved_this_turn(ctx) -> bool:
    state = ctx.session.turn_state
    return state.entered_play_turn.get(ctx.attacker.entity_id) == state.turn_number

from spirit.game.session.effects import full_stack


async def surf_back(ctx):
    await ctx.deal_damage()
    if ctx.attacker not in ctx.knockouts and await ctx.ask_yes_no("Shuffle this Pokémon and all attached cards into your deck?"):
        await ctx.shuffle_into_deck(full_stack(ctx.attacker), ctx.player_id)


card = PokemonCardDef(
    guid="e840e662-0a17-5148-9731-76de832f7ff3",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gholdengo.Name",
    display_name="Gholdengo",
    searchable_by=["Gholdengo", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=131,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gimmighoul.Name",
    family_id=999,
    abilities=[
        Attack(
            title="Strike It Rich",
            game_text="If this Pokémon evolved from Gimmighoul during this turn, this attack does 90 more damage.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_evolved_this_turn, 90),
        ),
        Attack(
            title="Surf Back",
            game_text="You may shuffle this Pokémon and all attached cards into your deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=surf_back,
        ),
    ],
)
