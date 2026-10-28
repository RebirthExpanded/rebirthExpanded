"""Swablu (SV3 169 -- JP SV3 094; English OBF/169). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="63e3e428-ef83-5f1e-a838-5e52db71e3c0",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    display_name="Swablu",
    searchable_by=["Swablu", "Basic"],
    subtypes=["Basic"],
    collector_number=169,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=333,
    abilities=[
        Attack(
            title="Fluffy Guard",
            game_text="During your opponent's next turn, this Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pc.protect_next_turn(reduce=20),
        ),
        Attack(
            title="Flap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
