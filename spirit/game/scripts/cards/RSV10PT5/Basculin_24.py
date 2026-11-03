"""Basculin (RSV10PT5 24 -- JP SV11W 021; English WHT/108, WHT/24). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="a94e1a03-5b66-5f8b-876c-227639f9c989",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Basculin.Name",
    display_name="Basculin",
    searchable_by=["Basculin", "Basic"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=550,
    abilities=[
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Bared Fangs",
            game_text="If your opponent's Active Pokémon has no damage counters on it before this attack does damage, this attack does nothing.",
            cost={PokemonTypes.WATER: 1},
            damage=50,
            effect=ac.bonus_if(ac.has_damage('defender'), 0, else_nothing=True),
        ),
    ],
)
