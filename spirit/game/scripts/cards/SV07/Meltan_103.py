"""Meltan (SV07 103 -- JP SV7 070; English SCR/103). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import is_pokemon_tool


card = PokemonCardDef(
    guid="e3a2378e-fd15-5eaa-8ae7-8b69f3ebbcca",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    display_name="Meltan",
    searchable_by=["Meltan", "Basic"],
    subtypes=["Basic"],
    collector_number=103,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=808,
    abilities=[
        Attack(
            title="Knickknack Carrying",
            game_text="Search your deck for a Pokémon Tool card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.METAL: 1},
            effect=su.search_to_hand(is_pokemon_tool, count=1, reveal=True, prompt="Choose a Pokémon Tool card."),
        ),
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
