"""Electivire (BWPJ 318 -- JP WAK 018; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="d4a228db-ecf4-5649-af32-12ded38ced41",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electivire.Name",
    display_name="Electivire",
    searchable_by=["Electivire", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=318,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    family_id=239,
    abilities=[
        Attack(
            title="Head Bolt",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Electroslug",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
