"""Hippopotas (ME3 39 -- JP M3 038; English POR/39). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="a35f6343-fba8-5af4-9c69-4ea9fe54f62a",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hippopotas.Name",
    display_name="Hippopotas",
    searchable_by=["Hippopotas", "Basic"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=449,
    abilities=[
        Attack(
            title="Sand Attack",
            game_text="During your opponent's next turn, if the Defending Pokémon tries to use an attack, your opponent flips a coin. If tails, that attack doesn't happen.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=ac.smokescreen_attack(),
        ),
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
