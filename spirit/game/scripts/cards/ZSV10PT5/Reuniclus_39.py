"""Reuniclus (ZSV10PT5 39 -- JP SV11B 042; English BLK/39, SVP/212). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

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

from spirit.game.session.effects import is_evolution_pokemon


async def cellular_ascension(ctx):
    for pokemon in list(ctx.my_bench()):
        await _evolve_from_deck(ctx, pokemon)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="5cf9a0da-13dd-57e8-a7ec-8d2ad143ecac",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reuniclus.Name",
    display_name="Reuniclus",
    searchable_by=["Reuniclus", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=39,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duosion.Name",
    family_id=577,
    abilities=[
        Attack(
            title="Cellular Ascension",
            game_text="For each of your Benched Pokémon, search your deck for a card that evolves from that Pokémon and put it onto that Pokémon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=cellular_ascension,
        ),
        Attack(
            title="Evo-Lariat",
            game_text="This attack does 40 more damage for each of your Evolution Pokémon in play.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=ac.damage_per(ac.count_in_play("mine", is_evolution_pokemon), 40, base=40),
        ),
    ],
)
