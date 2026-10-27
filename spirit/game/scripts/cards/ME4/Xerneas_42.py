"""Xerneas (ME4 42 -- JP M4 042; English CRI/42, CRI/91). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="74c4e511-c744-5745-80e6-c6b643e72839",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xerneas.Name",
    display_name="Xerneas",
    searchable_by=["Xerneas", "Basic"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=716,
    abilities=[
        Attack(
            title="Geo Storm",
            game_text="This attack does 30 damage for each Psychic Energy attached to all of your Pokémon.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=30,
            damage_operator="x",
            effect=ac.damage_per(ac.count_energy("mine", PokemonTypes.PSYCHIC), 30),
        ),
    ],
)
