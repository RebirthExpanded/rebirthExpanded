"""Tepig (MEP 50 -- JP MP 114; English MEP/50). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="349d1754-4fd3-51bc-86ec-867405a45067",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tepig.Name",
    display_name="Tepig",
    searchable_by=["Tepig", "Basic"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="MEP",
    regulation_mark="J",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=498,
    abilities=[
        Attack(
            title="Ember",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 2},
            damage=40,
            effect=ac.self_energy_discard_attack(1),
        ),
    ],
)
