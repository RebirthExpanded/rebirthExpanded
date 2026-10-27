"""Duraludon (SV08 129 -- JP SV7a 036; English SSP/129). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="8fb75a93-d47a-5081-a3b6-aa84343ddbd5",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duraludon.Name",
    display_name="Duraludon",
    searchable_by=["Duraludon", "Basic"],
    subtypes=["Basic"],
    collector_number=129,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=884,
    abilities=[
        Attack(
            title="Confront",
            game_text="",
            cost={PokemonTypes.METAL: 2},
            damage=50,
        ),
        Attack(
            title="Duralubeam",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.METAL: 3},
            damage=130,
            effect=ac.self_energy_discard_attack(count=2),
        ),
    ],
)
