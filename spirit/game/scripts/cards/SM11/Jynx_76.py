"""Jynx (SM - Unified Minds 76/236 -- JP SM11 032/094).

Basic Psychic Pokemon. HP 80, weakness Psychic x2, retreat 1.

  Ability  Ominous Posture  Once during your turn (before your attack), you
                            may move 1 damage counter from 1 of your
                            Pokemon to another of your Pokemon.
  Attract Smack  [PC] 30  Flip a coin. If heads, your opponent's Active
                          Pokemon is now Paralyzed.

Offered only with a damaged Pokemon and a second Pokemon to receive the
counter; the move is heal + counter placement in one step.
"""

from spirit.game.attributes import (AttrID, PokemonStage, PokemonTypes,
                                    Rarities, SpecialConditions)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)
from spirit.game.session.passives import effective_max_hp


def _damaged(board, pokemon) -> bool:
    return effective_max_hp(board, pokemon) > pokemon.get_attribute(AttrID.HP, 0)


def _ominous_posture_condition(board, player_id, pokemon=None) -> bool:
    mine = board.pokemon_in_play(player_id)
    return len(mine) >= 2 and any(_damaged(board, p) for p in mine)


async def ominous_posture(ctx):
    mine = ctx.my_pokemon_in_play()
    sources = [p for p in mine if _damaged(ctx.board, p)]
    if not sources or len(mine) < 2:
        return
    source = await ctx.choose_pokemon(
        sources, "Choose a Pokémon to move a damage counter from")
    if source is None:
        return
    dest = await ctx.choose_pokemon(
        [p for p in mine if p is not source],
        "Choose a Pokémon to move the damage counter to")
    if dest is None:
        return
    await ctx.move_damage_counters(source, dest, max_count=1)


card = PokemonCardDef(
    guid="55bb220c-e640-51a8-9452-0656e46b17f0",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name",
    display_name="Jynx",
    searchable_by=["Jynx", "Basic"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="SM11",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=124,
    abilities=[
        Ability(
            title="Ominous Posture",
            game_text="Once during your turn (before your attack), you may move 1 damage counter from 1 of your Pokémon to another of your Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_ominous_posture_condition,
            effect=ominous_posture,
        ),
        Attack(
            title="Attract Smack",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
