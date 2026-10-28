"""Lapras (SV035 131 -- JP SV2a 131; English MEW/131). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


card = PokemonCardDef(
    guid="49c321ab-e898-5e8b-b49f-2806bfdcf531",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name",
    display_name="Lapras",
    searchable_by=["Lapras", "Basic"],
    subtypes=["Basic"],
    collector_number=131,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=131,
    abilities=[
        Attack(
            title="Hop on My Back",
            game_text="Search your deck for up to 2 Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=su.search_to_hand(is_pokemon_card, count=2, reveal=True, prompt="Choose up to 2 Pokémon."),
        ),
        Attack(
            title="Aqua Edge",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
