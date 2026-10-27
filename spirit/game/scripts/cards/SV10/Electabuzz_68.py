"""Electabuzz (SV10 68 -- JP SV9a 034; English DRI/68). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="e30d7a83-ba74-5a85-bc53-acec112bb6a5",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    display_name="Electabuzz",
    searchable_by=["Electabuzz", "Basic"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=239,
    abilities=[
        Attack(
            title="Electroslug",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
