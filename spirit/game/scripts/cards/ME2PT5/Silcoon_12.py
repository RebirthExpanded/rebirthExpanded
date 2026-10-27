"""Silcoon (ME2PT5 12 -- JP M2a 005; English ASC/12). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.data_utils import def_for, subtypes_for

from spirit.game.session.passives import effective_bench_capacity


def _cocoon(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", "") in ("Silcoon", "Cascoon")


async def multiplying_cocoon(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    if effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench()) <= 0:
        return
    if not await ctx.ask_yes_no("Use Multiplying Cocoon?"):
        return
    picks = await ctx.search_deck(_cocoon, count=1, minimum=0, prompt="Choose a Silcoon or a Cascoon to put onto your Bench.")
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="0c747234-391d-53d6-bc0b-4128ae4c2655",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Silcoon.Name",
    display_name="Silcoon",
    searchable_by=["Silcoon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name",
    family_id=265,
    abilities=[
        Ability(
            title="Multiplying Cocoon",
            game_text="Once during your turn, when you play this Pokémon from your hand to evolve 1 of your Pokémon, you may use this Ability. Search your deck for a Silcoon or a Cascoon and put it onto your Bench. Then, shuffle your deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=multiplying_cocoon,
        ),
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
    ],
)
