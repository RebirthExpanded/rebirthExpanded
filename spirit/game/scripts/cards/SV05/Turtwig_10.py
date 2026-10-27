"""Turtwig (SV05 10 -- JP SV5K 003; English TEF/10). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="6da1bde9-f4ac-5323-bacd-a392577bb294",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtwig.Name",
    display_name="Turtwig",
    searchable_by=["Turtwig", "Basic"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=387,
    abilities=[
        Ability(
            title="Solid Shell",
            game_text="This Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            passive=pc.takes_less_passive(20),
        ),
        Attack(
            title="Leafage",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
