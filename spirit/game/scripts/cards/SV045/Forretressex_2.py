"""Forretress ex (SV045 2 -- JP SV2D 005; English PAF/2, PAF/212, PAL/230, PAL/5). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_grass(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.GRASS)


def _exploding_condition(board, player_id, pokemon) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def exploding_energy(ctx):
    picks = await ctx.search_deck(_basic_grass, count=5, minimum=0, prompt="Choose up to 5 Basic Grass Energy cards to attach")
    for card in picks:
        target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon to attach it to")
        if target is not None:
            await ctx.attach_energy(card, target)
    await ctx.shuffle_deck()
    await ctx.knock_out(ctx.source)


card = PokemonCardDef(
    guid="814ce819-4426-57da-9936-22368d8d0506",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Forretressex.Name",
    display_name="Forretress ex",
    searchable_by=["Forretress ex", "Stage 1", "ex", "Tera"],
    subtypes=["Stage 1", "ex", "Tera"],
    collector_number=2,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    family_id=204,
    passive=TeraRulePassive(),
    abilities=[
        Ability(
            title="Exploding Energy",
            game_text="Once during your turn, you may search your deck for up to 5 Basic Grass Energy cards and attach them to your Pokémon in any way you like. Then, shuffle your deck. If you searched your deck in this way, this Pokémon is Knocked Out.",
            activation=Activations.ONCE_PER_TURN,
            condition=_exploding_condition,
            effect=exploding_energy,
            self_knockout=True,
        ),
        Attack(
            title="Guard Press",
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 2},
            damage=120,
            effect=pc.protect_next_turn(reduce=30),
        ),
    ],
)
