"""Pelipper (SVP 22 -- JP SV2P 059; English PAF/204, PAL/159, SVP/22). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_supporter_card


async def hearsay(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    if not await ctx.ask_yes_no("Use Hearsay?"):
        return
    index = await ctx.choose("Choose 1", ["A Supporter card from your discard pile", "Search your deck for a Supporter card"])
    if index == 0:
        pool = [c for c in ctx.discard_pile() if is_supporter_card(c)]
        if pool:
            picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Supporter card")
            if picks:
                await ctx.put_in_hand(picks)
    else:
        picks = await ctx.search_deck(is_supporter_card, count=1, minimum=0, prompt="Choose a Supporter card.")
        if picks:
            await ctx.put_in_hand(picks)
        await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="567fd514-759e-5130-a7c3-7c2a7efab726",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pelipper.Name",
    display_name="Pelipper",
    searchable_by=["Pelipper", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wingull.Name",
    family_id=278,
    abilities=[
        Ability(
            title="Hearsay",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may choose 1: put a Supporter card from your discard pile into your hand; or search your deck for a Supporter card, reveal it, put it into your hand, and then shuffle your deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=hearsay,
        ),
        Attack(
            title="Wing Attack",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)
