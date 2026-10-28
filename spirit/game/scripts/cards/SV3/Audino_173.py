"""Audino (SV3 173 -- JP SVD 097; English OBF/173). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


card = PokemonCardDef(
    guid="9a83f907-c8f0-5baa-a042-a879c1cfdc29",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Audino.Name",
    display_name="Audino",
    searchable_by=["Audino", "Basic"],
    subtypes=["Basic"],
    collector_number=173,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=531,
    abilities=[
        Attack(
            title="Find a Friend",
            game_text="Search your deck for a Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(is_pokemon_card, count=1, reveal=True, prompt="Choose a Pokémon."),
        ),
        Attack(
            title="Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
