"""Oricorio (Promo_SWSH 210 -- JP SP 242; English SP/210). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_pokemon_card, is_supporter_card


async def _mixed_call(ctx):
    found = []
    for pred, what in ((is_pokemon_card, "a Pokémon"), (is_supporter_card, "a Supporter card")):
        picks = await ctx.search_deck(pred, 1, minimum=0, prompt=f"Choose {what}.")
        found += picks or []
    if found:
        await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="2eb80493-0867-5d95-a170-a7d1ca7d7765",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name",
    display_name="Oricorio",
    searchable_by=["Oricorio", "Basic", "Fusion Strike"],
    subtypes=["Basic", "Fusion Strike"],
    collector_number=210,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=741,
    abilities=[
        Attack(
            title="Mixed Call",
            game_text="Search your deck for a Pokémon and a Supporter card, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_mixed_call,
        ),
        Attack(
            title="Razor Wing",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
