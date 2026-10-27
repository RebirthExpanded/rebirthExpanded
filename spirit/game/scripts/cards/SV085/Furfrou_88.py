"""Furfrou (SV085 88 -- JP SVM 110; English PRE/88). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="3a2e98c9-d204-564a-90ed-5a04fdf059eb",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Furfrou.Name",
    display_name="Furfrou",
    searchable_by=["Furfrou", "Basic"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=676,
    abilities=[
        Ability(
            title="Fur Coat",
            game_text="This Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            passive=pc.takes_less_passive(20),
        ),
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
