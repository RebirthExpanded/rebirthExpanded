"""Dratini (SV035 147 -- JP SV2a 147; English MEW/147). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="e0e4ec96-2597-5e93-b161-b0c9b2dc119b",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    display_name="Dratini",
    searchable_by=["Dratini", "Basic"],
    subtypes=["Basic"],
    collector_number=147,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=147,
    abilities=[
        Attack(
            title="Beat",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Draconic Whip",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=40,
        ),
    ],
)
