"""Magmortar (BWPJ 307 -- JP WAK 007; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="46fa4a51-5169-54d6-8e14-c6f033315632",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmortar.Name",
    display_name="Magmortar",
    searchable_by=["Magmortar", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=307,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    family_id=240,
    abilities=[
        Attack(
            title="Magma Punch",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title="Fire Spin",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=ac.self_energy_discard_attack(2),
        ),
    ],
)
