"""Ninjask (BW - Dragons Exalted 11/124 -- JP BW5 005/050, the art here).

Stage 1 Grass Pokemon (evolves from Nincada). HP 60, weakness Fire x2,
retreat 1.

  Cast-off Shell  (Ability)  When you play this Pokemon from your hand to
                             evolve 1 of your Pokemon, you may search your
                             deck for Shedinja and put it onto your Bench.
                             Shuffle your deck afterward.
  Night Slash     [GC] 60    You may switch this Pokemon with 1 of your
                             Benched Pokemon.

Vivid Voltage Ninjask's Ability with a different attack; the Shedinja it
fetches is the one whose own rules text says it can only come into play
this way.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers, def_for


def _is_shedinja(card) -> bool:
    definition = def_for(card.archetype_id)
    return bool(definition) and definition.display_name == "Shedinja"


async def cast_off_shell(ctx):
    if not await ctx.ask_yes_no(
            "Search your deck for Shedinja and put it onto your Bench?"):
        return
    picks = await ctx.search_deck(
        _is_shedinja, count=1, minimum=0,
        prompt="Choose Shedinja to put onto your Bench.")
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


async def night_slash(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench:
        return
    if not await ctx.ask_yes_no("Switch this Pokémon with 1 of your Benched Pokémon?"):
        return
    target = await ctx.choose_pokemon(bench, "Choose a Pokémon to switch in")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


card = PokemonCardDef(
    guid="4ad1e874-3fc9-5b38-b094-bca24f582079",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninjask.Name",
    display_name="Ninjask",
    searchable_by=["Ninjask", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Ability(
            title="Cast-off Shell",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon, you may search your deck for Shedinja and put it onto your Bench. Shuffle your deck afterward.",
            trigger=Triggers.ON_EVOLVE,
            effect=cast_off_shell,
        ),
        Attack(
            title="Night Slash",
            game_text="You may switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=night_slash,
        ),
    ],
)
