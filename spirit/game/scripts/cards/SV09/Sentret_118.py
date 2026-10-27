"""Sentret (SV09 118 -- JP SV9 076; English JTG/118). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="295e9a50-00d8-5316-8c4e-5eb0cda15297",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sentret.Name",
    display_name="Sentret",
    searchable_by=["Sentret", "Basic"],
    subtypes=["Basic"],
    collector_number=118,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=161,
    abilities=[
        Attack(
            title="Smack",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
