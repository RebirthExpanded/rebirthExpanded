"""Noibat (ME2PT5 156 -- JP M2a 130; English ASC/156). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import is_pokemon_tool


card = PokemonCardDef(
    guid="2d818a59-8fc4-5159-9c77-53e5a0835850",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name",
    display_name="Noibat",
    searchable_by=["Noibat", "Basic"],
    subtypes=["Basic"],
    collector_number=156,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=714,
    abilities=[
        Attack(
            title="Knickknack Carrying",
            game_text="Search your deck for a Pokémon Tool card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(is_pokemon_tool, count=1, reveal=True, prompt="Choose a Pokémon Tool card."),
        ),
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1},
            damage=30,
        ),
    ],
)
