"""Misdreavus (ME2PT5 85 -- JP M2a 067; English ASC/233, ASC/85). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


async def _evolve_from_deck(ctx, pokemon) -> bool:
    logic_name = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    if not logic_name:
        return False
    picks = await ctx.search_deck(
        lambda c, name=logic_name: c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name,
        count=1, minimum=0, prompt="Choose a card that evolves from this Pokémon.")
    if picks:
        await ctx.evolve_pokemon(pokemon, picks[0])
        return True
    return False


async def ascension(ctx):
    await _evolve_from_deck(ctx, ctx.attacker)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="7088f612-c4da-542a-885d-a4eda8820de3",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name",
    display_name="Misdreavus",
    searchable_by=["Misdreavus", "Basic"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=200,
    abilities=[
        Attack(
            title="Ascension",
            game_text="Search your deck for a card that evolves from this Pokémon and put it onto this Pokémon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=ascension,
        ),
    ],
)
