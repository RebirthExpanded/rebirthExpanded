"""Bombirdier (SV1 138 -- JP SV1V 056; English SVI/138, SVI/219). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_pokemon_tool


card = PokemonCardDef(
    guid="d1b6e678-ee3d-5183-b196-805a7904639d",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bombirdier.Name",
    display_name="Bombirdier",
    searchable_by=["Bombirdier", "Basic"],
    subtypes=["Basic"],
    collector_number=138,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=962,
    abilities=[
        Attack(
            title="Knickknack Carrying",
            game_text="Search your deck for up to 3 Pokémon Tool cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(is_pokemon_tool, count=3, reveal=True, prompt="Choose up to 3 Pokémon Tool cards."),
        ),
        Attack(
            title="Clutch",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=ac.condition_attack(no_retreat=True),
        ),
    ],
)
