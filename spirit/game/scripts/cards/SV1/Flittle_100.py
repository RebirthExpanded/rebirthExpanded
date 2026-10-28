"""Flittle (SV1 100 -- JP SVAW 007; English SVI/100). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="0d55848b-7d31-5729-a044-0d410925070b",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name",
    display_name="Flittle",
    searchable_by=["Flittle", "Basic"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=955,
    abilities=[
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
