"""Oddish (SV3 1 -- JP SV3 001; English OBF/1). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="8851766a-54ce-5268-8d80-66fd23a6e67c",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name",
    display_name="Oddish",
    searchable_by=["Oddish", "Basic"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=43,
    abilities=[
        Attack(
            title="Feelin' Fine",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.draw_attack(1),
        ),
        Attack(
            title="Stampede",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
