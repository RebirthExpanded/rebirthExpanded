"""Rescue Team DX Pikachu (SPJ 36 -- JP SP 036; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


card = PokemonCardDef(
    guid="bcdaa0e9-f7d0-5b43-8276-2222f6c91b6a",
    key="SPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RescueTeamDXPikachu.Name",
    display_name="Rescue Team DX Pikachu",
    searchable_by=["Rescue Team DX Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="SPJ",
    regulation_mark="D",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Friend Rescue",
            game_text="Put a Pokémon from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.recover_from_discard(is_pokemon_card, count=1, reveal=True, prompt="Choose a Pokémon to put into your hand."),
        ),
        Attack(
            title="Electro Ball",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
