"""Team Rocket's Nidorina (SV10 115 -- JP SV10 059; English DRI/115). Japanese art.
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


def _darkness(pokemon) -> bool:
    return PokemonTypes.DARKNESS.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


async def dark_awakening(ctx):
    chosen = []
    pool = [p for p in ctx.my_pokemon_in_play() if _darkness(p)]
    while pool and len(chosen) < 2:
        pick = await ctx.choose_cards(pool, 1, minimum=0, prompt="Choose a Darkness Pokémon to evolve (Done to stop)")
        if not pick:
            break
        chosen.append(pick[0])
        pool = [p for p in pool if p is not pick[0]]
    for pokemon in chosen:
        await _evolve_from_deck(ctx, pokemon)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="b9ae46cd-cbdc-504b-8b4c-4c002a188667",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsNidorina.Name",
    display_name="Team Rocket's Nidorina",
    searchable_by=["Team Rocket's Nidorina", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=115,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsNidoranFemale.Name",
    family_id=29,
    abilities=[
        Attack(
            title="Dark Awakening",
            game_text="Choose up to 2 of your Darkness Pokémon. For each of those Pokémon, search your deck for a card that evolves from that Pokémon and put it onto that Pokémon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=dark_awakening,
        ),
        Attack(
            title="Scratch",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2},
            damage=50,
        ),
    ],
)
