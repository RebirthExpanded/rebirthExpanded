"""Geodude (SV035 74 -- JP SV2a 074; English MEW/74). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="d1b938b2-db62-5ef2-8a61-61b27164c39e",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name",
    display_name="Geodude",
    searchable_by=["Geodude", "Basic"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=74,
    abilities=[
        Attack(
            title="Stiffen",
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1},
            effect=pc.protect_next_turn(reduce=30),
        ),
        Attack(
            title="Knuckle Punch",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
