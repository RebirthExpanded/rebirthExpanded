"""Iron Bundle (SV4 56 -- JP SV4M 020; English PAR/56, SVP/58, SVP/66). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import full_stack, is_evolution_pokemon


def _blower_condition(board, player_id, pokemon) -> bool:
    other = next((pid for pid in board.player_ids if pid != player_id), None)
    obench = board.find_player_area(other, "bench") if other else None
    return pokemon._containing_area_name() == "bench" and bool(obench and obench.children)


async def hyper_blower(ctx):
    me = ctx.source
    new = await su.opponent_switches(ctx)
    if new is not None:
        await ctx.discard_cards(full_stack(me))


async def refrigerated_stream(ctx):
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is not None and d not in ctx.knockouts and is_evolution_pokemon(d):
        ac.lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="9f45f802-3be6-5d7b-9064-de148b7103f4",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronBundle.Name",
    display_name="Iron Bundle",
    searchable_by=["Iron Bundle", "Basic", "Future"],
    subtypes=["Basic", "Future"],
    collector_number=56,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=991,
    abilities=[
        Ability(
            title="Hyper Blower",
            game_text="Once during your turn, if this Pokémon is on your Bench, you may switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.) If you do, discard this Pokémon and all attached cards.",
            activation=Activations.ONCE_PER_TURN,
            condition=_blower_condition,
            effect=hyper_blower,
        ),
        Attack(
            title="Refrigerated Stream",
            game_text="If the Defending Pokémon is an Evolution Pokémon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=refrigerated_stream,
        ),
    ],
)
