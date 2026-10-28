"""Minior (SV4 99 -- JP SV3a 030; English PAR/201, PAR/99). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.passives import effective_retreat_cost


def _defender_retreat(ctx) -> int:
    d = ctx.opponent_active()
    return effective_retreat_cost(ctx.board, d) if d is not None else 0


async def far_flying_meteor(ctx):
    me = ctx.source
    if getattr(ctx, "energy_receiver", None) is not me or getattr(ctx, "attaching_player_id", None) != me.owning_player_id:
        return
    if me._containing_area_name() != "bench":
        return
    state = ctx.session.turn_state
    if getattr(me, "_meteor_turn", None) == state.turn_number:
        return
    if await ctx.ask_yes_no("Use Far-Flying Meteor?"):
        me._meteor_turn = state.turn_number
        await ctx.switch_active(ctx.player_id, me)


card = PokemonCardDef(
    guid="4ac95bd9-99ff-501c-a7af-e96b8bb9d165",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minior.Name",
    display_name="Minior",
    searchable_by=["Minior", "Basic"],
    subtypes=["Basic"],
    collector_number=99,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=774,
    abilities=[
        Ability(
            title="Far-Flying Meteor",
            game_text="Once during your turn, if this Pokémon is on your Bench, when you attach an Energy card from your hand to this Pokémon, you may switch it with your Active Pokémon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=far_flying_meteor,
        ),
        Attack(
            title="Gravitational Tackle",
            game_text="This attack does 20 damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=ac.damage_per(_defender_retreat, 20),
        ),
    ],
)
