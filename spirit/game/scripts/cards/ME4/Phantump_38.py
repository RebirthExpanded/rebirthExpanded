"""Phantump (ME4 38 -- JP M4 038; English CRI/38). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES



def _spiteful_cards(board, player_id, pokemon):
    hand = board.find_player_area(player_id, "hand")
    name = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    return [c for c in (hand.children if hand else []) if su.evolves_from(c, name)]


def _spiteful_ok(board, player_id, pokemon) -> bool:
    ts = getattr(board, "turn_state", None)
    return ts is not None and ts.turn_number > 2 and bool(_spiteful_cards(board, player_id, pokemon))


async def spiteful_evolution(ctx):
    me = ctx.source
    cards = _spiteful_cards(ctx.board, ctx.player_id, me)
    if not cards:
        return
    picks = await ctx.choose_cards(cards, 1, minimum=0, prompt="Choose a card that evolves from this Pokémon")
    if picks and await ctx.evolve_pokemon(me, picks[0]):
        evolved = picks[0]
        await ctx.deal_damage(20, target=evolved, apply_modifiers=False, as_counters=True, is_attack=False)


card = PokemonCardDef(
    guid="c5c61555-d9a3-57a7-8588-d639be6bd10f",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name",
    display_name="Phantump",
    searchable_by=["Phantump", "Basic"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=708,
    abilities=[
        Ability(
            title="Spiteful Evolution",
            game_text="Once during your turn, you may use this Ability. Choose a card in your hand that evolves from this Pokémon and put it onto this Pokémon to evolve it. If you do, place 2 damage counters on the Pokémon you evolved in this way. You can't use this Ability during your first turn.",
            activation=Activations.ONCE_PER_TURN,
            condition=_spiteful_ok,
            effect=spiteful_evolution,
        ),
        Attack(
            title="Mumble",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
