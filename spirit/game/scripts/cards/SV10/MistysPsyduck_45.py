from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.effects import full_stack


def _flustered_leap_condition(board, player_id, pokemon) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return not is_in_active_spot(pokemon) and bool(deck and deck.children)


async def flustered_leap(ctx):
    """Discard the bottom card of your deck; if you do, discard everything
    attached to this Benched Pokemon and put it on top of your deck."""
    deck = ctx.board.find_player_area(ctx.player_id, "deck")
    if not deck or not deck.children:
        return
    await ctx.discard_cards([deck.children[0]])
    pokemon = ctx.source
    attached = [c for c in full_stack(pokemon) if c is not pokemon]
    if attached:
        await ctx.discard_cards(attached)
    if await ctx.put_on_top_of_deck(pokemon):
        ctx.session.clear_pokemon_effects(pokemon)
        ctx.session.reset_pokemon_damage(pokemon)
        ctx.session.reset_ability_usage(pokemon)

card = PokemonCardDef(
    guid="e86515fe-bdbc-5fe2-9c4e-83202ca3cbed",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysPsyduck.Name",
    display_name="Misty's Psyduck",
    searchable_by=["Misty's Psyduck", "Basic", "MistysPsyduck"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=54,
    abilities=[
        Ability(
            title="Flustered Leap",
            game_text="Once during your turn, if this Pok\u00e9mon is on your Bench, you may discard the bottom card of your deck. If you do, discard all cards from this Pok\u00e9mon and put this Pok\u00e9mon on top of your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_flustered_leap_condition,
            effect=flustered_leap,
        ),
        Attack(
            title="Sprinkle Water",
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
    ],
)
