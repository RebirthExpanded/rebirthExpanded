"""Flittle (SV1 102 -- JP SV1S 036; English SVI/102). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="aff397a5-2372-5d81-9e5b-b445ef85e663",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name",
    display_name="Flittle",
    searchable_by=["Flittle", "Basic"],
    subtypes=["Basic"],
    collector_number=102,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=955,
    abilities=[
        Attack(
            title="Dash Off",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=su.switch_self_attack(),
        ),
    ],
)
