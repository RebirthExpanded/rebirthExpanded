"""Cornerstone Mask Ogerpon (SV10 111 -- JP SV9a 049; English DRI/111). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fighting(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIGHTING)
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="87a10e23-28e5-5680-9ed7-20cdc551c690",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CornerstoneMaskOgerpon.Name",
    display_name="Cornerstone Mask Ogerpon",
    searchable_by=["Cornerstone Mask Ogerpon", "Basic"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=1017,
    abilities=[
        Attack(
            title="Rock Kagura",
            game_text="Search your deck for a Basic Fighting Energy card and attach it to 1 of your Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_attach_energy(_basic_fighting, count=1, prompt="Choose a Basic Fighting Energy card to attach to 1 of your Pokémon."),
        ),
        Attack(
            title="Mountain Ramming",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=ac.mill_attack(1),
        ),
    ],
)
