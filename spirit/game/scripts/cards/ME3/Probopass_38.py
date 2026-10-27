"""Probopass (ME3 38 -- JP M3 037; English POR/38, POR/96). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="867deb57-b3ad-5eb2-9398-acba7ed6902a",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Probopass.Name",
    display_name="Probopass",
    searchable_by=["Probopass", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name",
    family_id=299,
    abilities=[
        Attack(
            title="Rolling Rocks",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
        ),
        Attack(
            title="Obliterating Nose",
            game_text="Discard 3 Energy from this Pokémon.",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=260,
            effect=ac.self_energy_discard_attack(count=3),
        ),
    ],
)
