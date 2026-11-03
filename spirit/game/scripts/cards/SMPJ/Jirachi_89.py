"""Jirachi (SMPJ 89 -- JP SMP 089; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import SpecialConditions


async def _five_color_wish(ctx):
    """Flip 5 coins. Draw a card for each heads."""
    results = await ctx.flip_coins(5, "Five Color Wish")
    heads = sum(1 for r in results if r)
    if heads:
        await ctx.draw_cards(heads)


card = PokemonCardDef(
    guid="f730e9be-924c-5126-ab1a-f31701d725aa",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi",
    searchable_by=["Jirachi", "Basic"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="SMPJ",
    regulation_mark="A",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=385,
    abilities=[
        Attack(
            title="Dream Invite",
            game_text="Both Active Pokémon are now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=ac.condition_attack(SpecialConditions.ASLEEP, both_actives=True),
        ),
        Attack(
            title="Five Color Wish",
            game_text="Flip 5 coins. Draw a card for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_five_color_wish,
        ),
    ],
)
