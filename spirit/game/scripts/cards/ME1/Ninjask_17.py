"""Ninjask (ME1 17 -- JP M1S 008; English MEG/137, MEG/17). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.data_utils import def_for, subtypes_for

from spirit.game.session.effects import is_pokemon_card
from spirit.game.session.passives import effective_bench_capacity


def _shedinja(card) -> bool:
    return is_pokemon_card(card) and getattr(def_for(card.archetype_id), "display_name", "") == "Shedinja"


async def cast_off_shell(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    if effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench()) <= 0:
        return
    if not await ctx.ask_yes_no("Use Cast-Off Shell?"):
        return
    picks = await ctx.search_deck(_shedinja, count=1, minimum=0, prompt="Choose a Shedinja to put onto your Bench.")
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="0a887251-fa62-5587-86e5-f014ec769b95",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninjask.Name",
    display_name="Ninjask",
    searchable_by=["Ninjask", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Ability(
            title="Cast-Off Shell",
            game_text="Once during your turn, when you play this Pokémon from your hand to evolve 1 of your Pokémon, you may use this Ability. Search your deck for a Shedinja and put it onto your Bench. Then, shuffle your deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=cast_off_shell,
        ),
        Attack(
            title="U-turn",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=su.switch_self_attack(),
        ),
    ],
)
