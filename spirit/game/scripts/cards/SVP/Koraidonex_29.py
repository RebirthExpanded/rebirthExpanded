"""Koraidon ex (SVP 29 -- JP SV1S 050; English PAF/245, SVI/125, SVI/231, SVI/247, SVI/254, SVP/29). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fighting(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIGHTING)
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])

from spirit.game.session.effects import is_basic_pokemon_in_play


def _dino_condition(board, player_id, pokemon) -> bool:
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(_basic_fighting(c) for c in discard.children)


async def dino_cry(ctx):
    targets = [p for p in ctx.my_pokemon_in_play() if is_basic_pokemon_in_play(p) and _of_type(p, PokemonTypes.FIGHTING)]
    pool = [c for c in ctx.discard_pile() if _basic_fighting(c)]
    if targets and pool:
        picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Attach up to 2 Basic Fighting Energy cards")
        for card in picks:
            target = await ctx.choose_pokemon(targets, "Choose 1 of your Basic Fighting Pokémon")
            if target is not None:
                await ctx.attach_energy(card, target)
    ctx.ends_turn = True


card = PokemonCardDef(
    guid="188630b0-83b3-5dfb-b5f4-93e114e8c59e",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koraidonex.Name",
    display_name="Koraidon ex",
    searchable_by=["Koraidon ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=29,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=230,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=1007,
    abilities=[
        Ability(
            title="Dino Cry",
            game_text="Once during your turn, you may attach up to 2 Basic Fighting Energy cards from your discard pile to your Basic Fighting Pokémon in any way you like. If you use this Ability, your turn ends.",
            activation=Activations.ONCE_PER_TURN,
            condition=_dino_condition,
            effect=dino_cry,
        ),
        Attack(
            title="Wild Impact",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=_hit_then_lock,
        ),
    ],
)
