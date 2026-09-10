"""Dusknoir (BW - Boundaries Crossed 63/149).

Stage 2 Psychic Pokemon. HP 130, weakness Darkness x2, no resistance,
retreat 3.

  Ability  Sinister Hand  As often as you like during your turn (before
                          your attack), you may move 1 damage counter from
                          1 of your opponent's Pokemon to another of your
                          opponent's Pokemon.

  Shadow Punch [PCCC] 60  This attack's damage isn't affected by
                          Resistance.

"As often as you like" is the whole point of the Ability, so one use keeps
asking for the next counter instead of closing after each one: the new
ctx.move_damage_counters_freely repeats [pick a damaged Pokemon of theirs,
declining is Done] -> [pick where the counter goes]. The activation stays
UNLIMITED as well, so re-opening it is still legal.

Both ends are the OPPONENT's board -- this shifts damage around their side
and never touches yours -- and the Ability wants two of their Pokemon in
play with a counter to move, or there is nothing to do.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import effective_max_hp


def _sinister_hand_condition(board, player_id, pokemon=None):
    """Two of the opponent's Pokemon in play, one of them with a counter."""
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    if opponent is None:
        return False
    theirs = board.pokemon_in_play(opponent)
    if len(theirs) < 2:
        return False
    return any(
        effective_max_hp(board, p) - p.get_attribute(AttrID.HP, 0) >= 10
        for p in theirs
    )


async def sinister_hand(ctx):
    """Shuffle damage around the opponent's board, one counter at a time."""
    theirs = ctx.opponent_pokemon_in_play()
    await ctx.move_damage_counters_freely(
        theirs, theirs,
        source_prompt="Choose an opponent's Pokémon to move a damage counter from (or Done)",
        dest_prompt="Choose an opponent's Pokémon to move the damage counter to",
    )


async def shadow_punch(ctx):
    """60, unaffected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="6770f291-f46b-549f-94ce-f569c3baccd8",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusknoir.Name",
    display_name="Dusknoir",
    searchable_by=["Dusknoir", "Stage 2", "Dusknoir"],
    subtypes=["Stage 2"],
    collector_number=63,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name",
    family_id=355,
    abilities=[
        Ability(
            title="Sinister Hand",
            game_text=(
                "As often as you like during your turn (before your attack), "
                "you may move 1 damage counter from 1 of your opponent's "
                "Pokémon to another of your opponent's Pokémon."
            ),
            activation=Activations.UNLIMITED,
            condition=_sinister_hand_condition,
            effect=sinister_hand,
        ),
        Attack(
            title="Shadow Punch",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=shadow_punch,
        ),
    ],
)
