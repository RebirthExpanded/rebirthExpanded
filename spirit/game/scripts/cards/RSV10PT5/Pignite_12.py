"""Pignite (RSV10PT5 12 -- JP SV11W 012; English WHT/12, WHT/97). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="f9e66b7f-33de-5212-b2a1-29c4b275f9e5",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pignite.Name",
    display_name="Pignite",
    searchable_by=["Pignite", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tepig.Name",
    family_id=498,
    abilities=[
        Attack(
            title="Combustion",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
        ),
        Attack(
            title="Heat Crash",
            game_text="",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)
