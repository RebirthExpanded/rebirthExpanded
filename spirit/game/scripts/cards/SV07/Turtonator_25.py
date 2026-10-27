"""Turtonator (SV07 25 -- JP SV7 015; English SCR/146, SCR/25). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="d008677b-ab79-52ad-afb1-95fae9dff260",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtonator.Name",
    display_name="Turtonator",
    searchable_by=["Turtonator", "Basic"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=776,
    abilities=[
        Attack(
            title="Ring of Fire",
            game_text="Your opponent's Active Pokémon is now Burned. During your opponent's next turn, that Pokémon can't retreat.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=ac.condition_attack(SpecialConditions.BURNED, no_retreat=True),
        ),
        Attack(
            title="Inferno Onrush",
            game_text="This Pokémon also does 60 damage to itself.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=ac.recoil_attack(60),
        ),
    ],
)
