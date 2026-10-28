"""Zangoose (SV1 146 -- JP SVAW 008; English SVI/146). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="54bcbf25-0df9-5202-bf9c-01ff553f4053",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zangoose.Name",
    display_name="Zangoose",
    searchable_by=["Zangoose", "Basic"],
    subtypes=["Basic"],
    collector_number=146,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=335,
    abilities=[
        Attack(
            title="Slash",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
