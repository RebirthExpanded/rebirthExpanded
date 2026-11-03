"""Sandile (BWPJ 408 -- JP CS1 008; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="e8459e5d-df96-5c74-a6ed-2998093a4081",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandile.Name",
    display_name="Sandile",
    searchable_by=["Sandile", "Basic"],
    subtypes=["Basic"],
    collector_number=408,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=551,
    abilities=[
        Attack(
            title="Sand Tomb",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=ac.condition_attack(no_retreat=True),
        ),
    ],
)
