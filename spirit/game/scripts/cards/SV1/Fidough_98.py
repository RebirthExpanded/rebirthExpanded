"""Fidough (SV1 98 -- JP SV1S 033; English SVI/213, SVI/98). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="6c9437b5-9971-55ad-93de-8f02cafa0ed6",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fidough.Name",
    display_name="Fidough",
    searchable_by=["Fidough", "Basic"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=926,
    abilities=[
        Attack(
            title="Springy",
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=pc.protect_next_turn(reduce=30),
        ),
        Attack(
            title="Flop",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
