"""Charmeleon (SV035 5 -- JP SV2a 005; English MEW/169, MEW/5). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="49775ed9-139d-5421-9978-1c1e4d34810b",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    display_name="Charmeleon",
    searchable_by=["Charmeleon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Combustion",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title="Fire Blast",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 3},
            damage=90,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
