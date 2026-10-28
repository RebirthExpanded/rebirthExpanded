"""Eevee (SV035 133 -- JP SV2a 133; English MEW/133). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.effects import is_pokemon_card


async def colorful_friends(ctx):
    got = []
    for _ in range(3):
        seen = set()
        for c in got:
            seen.update(c.get_attribute(AttrID.POKEMON_TYPES) or [])
        picks = await ctx.search_deck(lambda c: is_pokemon_card(c) and not (set(c.get_attribute(AttrID.POKEMON_TYPES) or []) & seen),
                                      count=1, minimum=0, prompt="Choose a Pokémon of a different type.")
        if not picks:
            break
        got += picks
    if got:
        await ctx.put_in_hand(got)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="e1e1b54f-8cce-5633-a7c1-57ba2e3e5987",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic"],
    subtypes=["Basic"],
    collector_number=133,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Colorful Friends",
            game_text="Search your deck for up to 3 Pokémon of different types, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=colorful_friends,
        ),
        Attack(
            title="Skip",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
