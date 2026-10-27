"""Eevee (SV065 50 -- JP SV6a 050; English SFA/50). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import def_for, subtypes_for


def _etype(card):
    return getattr(def_for(card.archetype_id), "display_name", "")


async def colorful_catch(ctx):
    got = []
    for _ in range(3):
        seen = {_etype(c) for c in got}
        picks = await ctx.search_deck(lambda c: is_basic_energy_card(c) and _etype(c) not in seen,
                                      count=1, minimum=0, prompt="Choose a Basic Energy card of a different type.")
        if not picks:
            break
        got += picks
        await ctx.put_in_hand(picks)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="8f403bb9-7fc0-5244-aa3b-4c5689fe5c24",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Colorful Catch",
            game_text="Search your deck for up to 3 Basic Energy cards of different types, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=colorful_catch,
        ),
        Attack(
            title="Headbutt",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
