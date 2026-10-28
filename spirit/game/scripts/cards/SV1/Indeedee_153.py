"""Indeedee (SV1 153 -- JP SV1V 063; English SVI/153). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
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


async def expert_nurturer(ctx):
    pool = list(ctx.my_pokemon_in_play())
    if pool:
        target = await ctx.choose_pokemon(pool, "Choose 1 of your Pokémon to evolve")
        if target is not None:
            await _evolve_from_deck(ctx, target)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="62056b98-8fb1-5630-8f3d-e7fbad807e6a",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Indeedee.Name",
    display_name="Indeedee",
    searchable_by=["Indeedee", "Basic"],
    subtypes=["Basic"],
    collector_number=153,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=876,
    abilities=[
        Attack(
            title="Expert Nurturer",
            game_text="Search your deck for a card that evolves from 1 of your Pokémon and put it onto that Pokémon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=expert_nurturer,
        ),
        Attack(
            title="Hypnoblast",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
