"""Dunsparce (SV2 156 -- JP SV2P 056; English PAL/156). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


card = PokemonCardDef(
    guid="e931182f-97d8-5d0b-8286-f21d72af6a4d",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dunsparce.Name",
    display_name="Dunsparce",
    searchable_by=["Dunsparce", "Basic"],
    subtypes=["Basic"],
    collector_number=156,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=206,
    abilities=[
        Attack(
            title="Find a Friend",
            game_text="Search your deck for a Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(is_pokemon_card, count=1, reveal=True, prompt="Choose a Pokémon."),
        ),
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)
