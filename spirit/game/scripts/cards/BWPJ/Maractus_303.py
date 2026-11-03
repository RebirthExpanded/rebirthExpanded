"""Maractus (BWPJ 303 -- JP WAK 003; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="885dec43-fb46-5d2f-ae04-69b9c6c0ee2a",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maractus.Name",
    display_name="Maractus",
    searchable_by=["Maractus", "Basic"],
    subtypes=["Basic"],
    collector_number=303,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=556,
    abilities=[
        Attack(
            title="Pounce",
            game_text="Flip a coin. If heads, this attack does 10 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=ac.flip_bonus(10),
        ),
    ],
)
