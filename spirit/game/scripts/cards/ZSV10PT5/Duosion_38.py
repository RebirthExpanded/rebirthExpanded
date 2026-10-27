"""Duosion (ZSV10PT5 38 -- JP SV11B 041; English BLK/119, BLK/38). Japanese art.
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


async def cellular_evolution(ctx):
    pool = list(ctx.my_pokemon_in_play())
    if pool:
        target = await ctx.choose_pokemon(pool, "Choose 1 of your Pokémon to evolve")
        if target is not None:
            await _evolve_from_deck(ctx, target)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="ff4d70ee-3279-5956-86ba-02313ed14b2c",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duosion.Name",
    display_name="Duosion",
    searchable_by=["Duosion", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Solosis.Name",
    family_id=577,
    abilities=[
        Attack(
            title="Cellular Evolution",
            game_text="Search your deck for a card that evolves from 1 of your Pokémon and put it onto that Pokémon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=cellular_evolution,
        ),
        Attack(
            title="Spray Fluid",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
