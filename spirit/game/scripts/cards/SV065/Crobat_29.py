"""Crobat (SV065 29 -- JP SV6a 029; English SFA/29). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _played_this_turn(ctx, display_name) -> bool:
    for archetype_id, _name, _type in ctx.session.turn_state.trainers_played:
        if getattr(def_for(archetype_id), "display_name", None) == display_name:
            return True
    return False



def _envoy_condition(board, player_id, pokemon) -> bool:
    from spirit.game.data_utils import def_for as _d
    ts = getattr(board, "turn_state", None)
    hand = board.find_player_area(player_id, "hand")
    return (ts is not None and len(hand.children if hand else []) < 8
            and any(getattr(_d(a), "display_name", None) == "Janine's Secret Art" for a, _n, _t in ts.trainers_played))


async def shadowy_envoy(ctx):
    if _played_this_turn(ctx, "Janine's Secret Art"):
        await ctx.draw_until(8)


card = PokemonCardDef(
    guid="f152a8f5-ffbb-5fb7-b070-dc904942d2b7",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name",
    display_name="Crobat",
    searchable_by=["Crobat", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=29,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Shadowy Envoy",
            game_text="Once during your turn, if you played Janine's Secret Art from your hand this turn, you may draw cards until you have 8 cards in your hand.",
            activation=Activations.ONCE_PER_TURN,
            condition=_envoy_condition,
            effect=shadowy_envoy,
        ),
        Attack(
            title="Poison Fang",
            game_text="Your opponent's Active Pokémon is now Poisoned. During Pokémon Checkup, put 2 damage counters on that Pokémon instead of 1.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=ac.condition_attack(SpecialConditions.POISONED, counters=2),
        ),
    ],
)
