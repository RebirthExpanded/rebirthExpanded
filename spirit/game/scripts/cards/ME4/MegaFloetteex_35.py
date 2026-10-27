"""Mega Floette ex (ME4 35 -- JP M4 035; English CRI/101, CRI/117, CRI/35). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_psychic(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.PSYCHIC)



async def gentle_light(ctx):
    for pokemon in list(ctx.my_pokemon_in_play()) + list(ctx.opponent_pokemon_in_play()):
        await ctx.heal(30, pokemon)


def _benched(pokemon) -> bool:
    return pokemon._containing_area_name() == "bench"


card = PokemonCardDef(
    guid="d4e773e2-7119-581c-b4c6-d75950340632",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaFloetteex.Name",
    display_name="Mega Floette ex",
    searchable_by=["Mega Floette ex", "Basic", "ex", "SV_Mega"],
    subtypes=["Basic", "ex", "SV_Mega"],
    collector_number=35,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=669,
    abilities=[
        Attack(
            title="Gentle Light",
            game_text="Heal 30 damage from each Pokémon (both yours and your opponent's).",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=gentle_light,
        ),
        Attack(
            title="Eternity Bloom",
            game_text="Search your deck for up to 4 Basic Psychic Energy cards and attach them to your Benched Pokémon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=200,
            effect=su.search_attach_energy(_basic_psychic, count=4, target_pred=_benched, prompt="Choose up to 4 Basic Psychic Energy cards to attach to your Benched Pokémon."),
        ),
    ],
)
