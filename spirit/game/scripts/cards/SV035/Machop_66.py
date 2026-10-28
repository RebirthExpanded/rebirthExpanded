"""Machop (SV035 66 -- JP SV2a 066; English MEW/66). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="f12a928c-e057-5c5e-b6a4-9069de7d0677",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name",
    display_name="Machop",
    searchable_by=["Machop", "Basic"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=66,
    abilities=[
        Attack(
            title="Mountain Mashing",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=ac.mill_attack(1),
        ),
        Attack(
            title="Punch",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)
