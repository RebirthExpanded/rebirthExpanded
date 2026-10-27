"""Sandshrew (ME6 35 -- JP M6 035; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


async def awakening(ctx):
    me = ctx.attacker
    name = me.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    picks = await ctx.search_deck(lambda c: su.evolves_from(c, name), count=1, minimum=0,
                                  prompt="Choose a card that evolves from this Pokémon.")
    if picks:
        await ctx.evolve_pokemon(me, picks[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="4606f7a6-8b3f-5fe4-a34e-342c708ac441",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name",
    display_name="Sandshrew",
    searchable_by=["Sandshrew", "Basic"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=27,
    abilities=[
        Attack(
            title="Awakening",
            game_text="Search your deck for a card that evolves from this Pokémon and put it onto this Pokémon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=awakening,
        ),
    ],
)
