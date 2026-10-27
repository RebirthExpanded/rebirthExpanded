"""Magmortar (ME6 13 -- JP M6 013; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card
from spirit.game.data_utils import def_for, subtypes_for



def _buddy_targets(board, player_id):
    return [p for p in board.pokemon_in_play(player_id)
            if getattr(def_for(p.archetype_id), "display_name", None) in ("Electivire", "Magmortar")]


def _fire(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIRE)


def _lightning(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.LIGHTNING)


def _buddy_ok(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(_buddy_targets(board, player_id)) and any(_fire(c) or _lightning(c) for c in (hand.children if hand else []))


async def buddy_boost(ctx):
    picks = []
    for pred, label in ((_fire, "Fire"), (_lightning, "Lightning")):
        pool = [c for c in ctx.hand() if pred(c)]
        if pool:
            picks += await ctx.choose_cards(pool, 1, minimum=0, prompt=f"Choose up to 1 Basic {label} Energy card to attach.")
    if picks:
        await su.distribute_energy(ctx, picks, _buddy_targets(ctx.board, ctx.player_id))


card = PokemonCardDef(
    guid="451841fd-dd26-5e96-a44a-90aed55e8e89",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmortar.Name",
    display_name="Magmortar",
    searchable_by=["Magmortar", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    family_id=240,
    abilities=[
        Ability(
            title="Buddy Boost",
            game_text="Once during your turn, you may use this Ability. Choose up to 1 Basic Fire Energy card and up to 1 Basic Lightning Energy card from your hand and attach them to your Electivire or Magmortar in any way you like.",
            activation=Activations.ONCE_PER_TURN,
            condition=_buddy_ok,
            effect=buddy_boost,
        ),
        Attack(
            title="Heat Stamp",
            game_text="",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)
