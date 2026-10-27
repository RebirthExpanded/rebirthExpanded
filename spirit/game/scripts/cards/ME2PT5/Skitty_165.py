"""Skitty (ME2PT5 165 -- JP MC 585; English ASC/165). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="2f2a2db0-c4ec-5cfa-afde-f0fb94df78fb",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    display_name="Skitty",
    searchable_by=["Skitty", "Basic"],
    subtypes=["Basic"],
    collector_number=165,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=300,
    abilities=[
        Attack(
            title="Cat Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
