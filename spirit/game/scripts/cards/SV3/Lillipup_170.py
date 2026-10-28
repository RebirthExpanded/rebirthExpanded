"""Lillipup (SV3 170 -- JP SVD 094; English OBF/170). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="4d464e71-d22f-5e50-bdf2-fb5f2fc2618b",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lillipup.Name",
    display_name="Lillipup",
    searchable_by=["Lillipup", "Basic"],
    subtypes=["Basic"],
    collector_number=170,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=506,
    abilities=[
        Attack(
            title="Rear Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
