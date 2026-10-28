"""Sinistea (SVP 62 -- JP SV2P 035; English OBF/97, SVP/62). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="98b9ea25-0a76-50e1-8b7f-8c4da91a3765",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sinistea.Name",
    display_name="Sinistea",
    searchable_by=["Sinistea", "Basic"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=854,
    abilities=[
        Attack(
            title="Cold Tea",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
