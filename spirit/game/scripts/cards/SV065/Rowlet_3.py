"""Rowlet (SV065 3 -- JP SV6a 003; English SFA/3). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="07c3a2a7-f7ce-598f-aa55-ddc40e290b77",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rowlet.Name",
    display_name="Rowlet",
    searchable_by=["Rowlet", "Basic"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=722,
    abilities=[
        Attack(
            title="Add On",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.draw_attack(1),
        ),
        Attack(
            title="Leafage",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
