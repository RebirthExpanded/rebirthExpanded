"""Glimmet (SV2 124 -- JP SV2P 042; English PAF/179, PAL/124). Japanese art.
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
    guid="cb4b6df4-42bc-51f1-bd04-d887d8eb66c3",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmet.Name",
    display_name="Glimmet",
    searchable_by=["Glimmet", "Basic"],
    subtypes=["Basic"],
    collector_number=124,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=969,
    abilities=[
        Attack(
            title="Ascension",
            game_text="Search your deck for a card that evolves from this Pokémon and put it onto this Pokémon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=ascension,
        ),
    ],
)
