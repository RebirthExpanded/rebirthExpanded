"""Mew-EX (BW - Dragons Exalted 46/124 -- JP BW5 022/050).

Basic Psychic Pokemon-EX. HP 120, weakness Psychic x2, retreat 1.

  Ability  Versatile  This Pokemon can use the attacks of any Pokemon in
                      play (both yours and your opponent's). (You still
                      need the necessary Energy to use each attack.)

  Replace  [P]  Move as many Energy attached to your Pokemon to your other
                Pokemon in any way you like.

The widest of the borrowing Abilities: every Pokemon on the table, the
opponent's included, and no stage filter -- an evolved attacker's attack is
on offer here as readily as a Basic's. Only Mew-EX itself is skipped.

Replace is Weavile-GX's free Energy shuffle without the type filter: the
player keeps moving Energy around their own board and stops when done.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import (BorrowedAttacksPassive,
                                              all_pokemon_in_play)
from spirit.game.data_utils import Ability, Attack, PokemonCardDef


async def replace(ctx):
    """Move your Energy around your board until the player is done."""
    pokemon = ctx.my_pokemon_in_play()
    await ctx.move_energy_freely(
        pokemon, pokemon,
        prompt="Choose an Energy to move (or Done)",
    )


card = PokemonCardDef(
    guid="0aee6137-8363-58fa-b006-c27b860a3dd0",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewEX.Name",
    display_name="Mew-EX",
    searchable_by=["Mew-EX", "Basic", "EX", "MewEX"],
    subtypes=["Basic", "EX"],
    collector_number=46,
    set_code="BW6",
    rarity=Rarities.RareHoloEX,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Ability(
            title="Versatile",
            game_text="This Pokémon can use the attacks of any Pokémon in play (both yours and your opponent's). (You still need the necessary Energy to use each attack.)",
            passive=BorrowedAttacksPassive(all_pokemon_in_play),
        ),
        Attack(
            title="Replace",
            game_text="Move as many Energy attached to your Pokémon to your other Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=replace,
        ),
    ],
)
