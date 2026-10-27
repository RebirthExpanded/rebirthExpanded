"""Helioptile (ME2PT5 63 -- JP M2a 052; English ASC/63). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="1727bc72-9b3a-58bb-9c18-9f877d97979e",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Helioptile.Name",
    display_name="Helioptile",
    searchable_by=["Helioptile", "Basic"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=694,
    abilities=[
        Attack(
            title="Zap Kick",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
