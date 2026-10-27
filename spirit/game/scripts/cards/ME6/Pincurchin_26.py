"""Pincurchin (ME6 26 -- JP M6 026; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="6ee61bb3-f0e7-50fc-b7e2-c82ecd6c441e",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pincurchin.Name",
    display_name="Pincurchin",
    searchable_by=["Pincurchin", "Basic"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=871,
    abilities=[
        Attack(
            title="Energy Crush",
            game_text="This attack does 20 damage for each Energy attached to all of your opponent's Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=ac.damage_per(ac.count_energy("opponent"), 20),
        ),
    ],
)
