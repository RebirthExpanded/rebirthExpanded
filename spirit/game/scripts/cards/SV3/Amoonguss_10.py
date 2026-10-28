"""Amoonguss (SV3 10 -- JP SV1a 003; English OBF/10). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="78e679ee-739b-56d7-9350-e23b0c98f5c6",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Amoonguss.Name",
    display_name="Amoonguss",
    searchable_by=["Amoonguss", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name",
    family_id=590,
    abilities=[
        Attack(
            title="Dangerous Spores",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, SpecialConditions.POISONED, flip=True),
        ),
    ],
)
