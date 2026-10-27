"""Bramblin (SV05 20 -- JP SV5M 012; English TEF/20). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="4f243fa8-8024-50ac-9aaf-ec7891129ea0",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bramblin.Name",
    display_name="Bramblin",
    searchable_by=["Bramblin", "Basic"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=946,
    abilities=[
        Attack(
            title="Spike Sting",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
