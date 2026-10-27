"""Arven's Greedent (SV10 159 -- JP SV9a 055; English DRI/159, DRI/205). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.data_utils import def_for, subtypes_for


async def greedy_order(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    pool = [c for c in ctx.discard_pile()
            if getattr(def_for(c.archetype_id), "display_name", "") == "Arven's Sandwich"]
    if not pool or not await ctx.ask_yes_no("Put up to 2 Arven's Sandwich cards from your discard pile into your hand?"):
        return
    picks = await ctx.choose_cards(pool, 2, minimum=0, prompt="Choose up to 2 Arven's Sandwich cards")
    if picks:
        await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="9cb796fe-ef63-5a1d-a1f5-2110e3414fa0",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensGreedent.Name",
    display_name="Arven's Greedent",
    searchable_by=["Arven's Greedent", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=159,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensSkwovet.Name",
    family_id=819,
    abilities=[
        Ability(
            title="Greedy Order",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may put up to 2 Arven's Sandwich cards from your discard pile into your hand.",
            trigger=Triggers.ON_EVOLVE,
            effect=greedy_order,
        ),
        Attack(
            title="Rolling Tackle",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
