"""Elekid (SV4 59 -- JP SV4M 022; English PAR/59). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="769655ad-2d4d-50c6-be79-4c6d4df62c2b",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Elekid.Name",
    display_name="Elekid",
    searchable_by=["Elekid", "Basic"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=239,
    abilities=[
        Attack(
            title="Crackling Shot",
            game_text="This attack does 30 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={},
            effect=ac.snipe_attack(30, pool="any"),
        ),
    ],
)
