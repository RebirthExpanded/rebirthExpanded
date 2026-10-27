"""Iron Thorns (SV05 62 -- JP SV5M 030; English SVP/98, TEF/62). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.data_utils import def_for, subtypes_for


def _has_sub(card, sub) -> bool:
    return card is not None and sub in (subtypes_for(card.archetype_id) or [])


async def destructo_press(ctx):
    top = list(ctx.deck_top(5))
    if not top:
        return
    await ctx.reveal_cards(top)
    futures = [c for c in top if _has_sub(c, "Future")]
    if futures:
        await ctx.deal_damage(70 * len(futures))
        await ctx.discard_cards(futures)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="cb8eeb30-c0c1-5040-b94c-be360bf4688f",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronThorns.Name",
    display_name="Iron Thorns",
    searchable_by=["Iron Thorns", "Basic", "Future"],
    subtypes=["Basic", "Future"],
    collector_number=62,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=995,
    abilities=[
        Attack(
            title="Destructo-Press",
            game_text="Reveal the top 5 cards of your deck. This attack does 70 damage for each Future card you find there. Then, discard those Future cards and shuffle the other cards back into your deck.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=destructo_press,
        ),
        Attack(
            title="Megaton Lariat",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)
