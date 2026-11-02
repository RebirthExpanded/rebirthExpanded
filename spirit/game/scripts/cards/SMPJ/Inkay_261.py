"""Inkay (SMPJ 261 -- JP SMP 261; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="7d47e48d-62d1-544c-85b7-293d726bb3cf",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    display_name="Inkay",
    searchable_by=["Inkay", "Basic"],
    subtypes=["Basic"],
    collector_number=261,
    set_code="SMPJ",
    regulation_mark="B",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=686,
    abilities=[
        Attack(
            title="Spray Ink",
            game_text="During your opponent's next turn, if the Defending Pokémon tries to attack, your opponent flips a coin. If tails, that attack doesn't happen.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=ac.smokescreen_attack(),
        ),
    ],
)
