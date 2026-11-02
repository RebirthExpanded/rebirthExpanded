"""Litten (MEP 44 -- JP MP 120; English MEP/44). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5fba7aeb-ad31-5382-93d8-79bd6f531d88",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Litten.Name",
    display_name="Litten",
    searchable_by=["Litten", "Basic"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="MEP",
    regulation_mark="J",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=725,
    abilities=[
        Attack(
            title="Fire Fang",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 2},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.BURNED),
        ),
    ],
)
