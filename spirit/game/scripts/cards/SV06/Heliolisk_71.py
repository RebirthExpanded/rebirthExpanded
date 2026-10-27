"""Heliolisk (SV06 71 -- JP SV5a 029; English TWM/177, TWM/71). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="0ee1daa8-bc36-5095-9be8-2d9dce77e46e",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heliolisk.Name",
    display_name="Heliolisk",
    searchable_by=["Heliolisk", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Helioptile.Name",
    family_id=694,
    abilities=[
        Attack(
            title="Wild Charge",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=70,
            effect=ac.recoil_attack(20),
        ),
    ],
)
