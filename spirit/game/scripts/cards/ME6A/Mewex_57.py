"""Mew ex (JP M6a 057/103 -- 30th Celebrations).

Basic Psychic Pokemon ex. HP 160, weakness Darkness x2, resistance
Fighting -30, no retreat cost, regulation mark J.

  Ability  Memory Spiral  This Pokemon can use all the attacks of your
                          Benched Pokemon. (You still need the necessary
                          Energy to use each attack.)

  Teleport Break  [P] 30  You may switch this Pokemon with 1 of your
                          Benched Pokemon.

The Bench, not the whole board: the attacks it borrows are the ones sitting
behind it, so an attacker parked on the Bench arms this one and evolved
Pokemon count as readily as Basics -- Memories of Dawn's Basic filter is not
here.

The English 30th Celebrations release is not out, so the names here are
this pool's rendering of きおくのらせん and テレポートブレイク and the
Japanese collector number stands.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import (BorrowedAttacksPassive,
                                              own_bench_pokemon)
from spirit.game.data_utils import Ability, Attack, PokemonCardDef


async def teleport_break(ctx):
    """30, then you may swap this Pokemon out for a Benched one."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench:
        return
    if not await ctx.ask_yes_no("Switch this Pokémon with 1 of your Benched Pokémon?"):
        return
    target = await ctx.choose_pokemon(bench, "Choose a Pokémon to switch to.")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


card = PokemonCardDef(
    guid="6879b0aa-729e-566f-a70e-23eed8a820e0",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewex.Name",
    display_name="Mew ex",
    searchable_by=["Mew ex", "Basic", "ex", "Mewex"],
    subtypes=["Basic", "ex"],
    collector_number=57,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=151,
    abilities=[
        Ability(
            title="Memory Spiral",
            game_text="This Pokémon can use all the attacks of your Benched Pokémon. (You still need the necessary Energy to use each attack.)",
            passive=BorrowedAttacksPassive(own_bench_pokemon),
        ),
        Attack(
            title="Teleport Break",
            game_text="You may switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=teleport_break,
        ),
    ],
)
