"""Wugtrio (SV3 59 -- JP SVD 031; English OBF/59). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="77c4baab-7f4a-562d-bdce-f095ebf7b4c2",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wugtrio.Name",
    display_name="Wugtrio",
    searchable_by=["Wugtrio", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name",
    family_id=960,
    abilities=[
        Attack(
            title="Entwining Entrapment",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.WATER: 1},
            damage=50,
            effect=ac.condition_attack(no_retreat=True),
        ),
    ],
)
