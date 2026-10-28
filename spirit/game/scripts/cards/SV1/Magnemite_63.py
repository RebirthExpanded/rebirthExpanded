"""Magnemite (SV1 63 -- JP SV1V 026; English SVI/63). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="e9756b86-3ec6-540f-a5ac-e2a7b054997d",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    display_name="Magnemite",
    searchable_by=["Magnemite", "Basic"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=81,
    abilities=[
        Attack(
            title="Magnetic Switch",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.switch_self_attack(),
        ),
        Attack(
            title="Electro Ball",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)
