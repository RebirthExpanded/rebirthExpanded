"""Swallowed up Pikachu (SPJ 105 -- JP SP 105; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="d215bad5-ddd0-5d73-84e7-aebb7b6d0855",
    key="SPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SwallowedupPikachu.Name",
    display_name="Swallowed up Pikachu",
    searchable_by=["Swallowed up Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=105,
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
            title="Struggle",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=ac.self_energy_discard_attack(all_energy=True),
        ),
    ],
)
