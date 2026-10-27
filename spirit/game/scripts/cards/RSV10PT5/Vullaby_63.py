"""Vullaby (RSV10PT5 63 -- JP SV11B 063; English WHT/144, WHT/63). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="71780f55-85f9-53f6-9ef1-cba7091c35d2",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vullaby.Name",
    display_name="Vullaby",
    searchable_by=["Vullaby", "Basic"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=629,
    abilities=[
        Attack(
            title="Playful Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
