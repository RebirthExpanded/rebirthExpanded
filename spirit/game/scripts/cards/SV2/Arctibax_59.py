"""Arctibax (SV2 59 -- JP SV2P 026; English PAF/129, PAL/209, PAL/59, SVP/64). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="c05c7e9a-dc9e-559e-a127-8cc3a4c8735c",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arctibax.Name",
    display_name="Arctibax",
    searchable_by=["Arctibax", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frigibax.Name",
    family_id=996,
    abilities=[
        Attack(
            title="Sharp Fin",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Frost Smash",
            game_text="",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)
