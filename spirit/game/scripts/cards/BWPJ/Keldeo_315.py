"""Keldeo (BWPJ 315 -- JP WAK 015; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="bf09cb97-9c5f-5085-abf8-1dce63c6fcdb",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Keldeo.Name",
    display_name="Keldeo",
    searchable_by=["Keldeo", "Basic"],
    subtypes=["Basic"],
    collector_number=315,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=647,
    abilities=[
        Attack(
            title="Spiral Drain",
            game_text="Heal 20 damage from this Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=su.heal_attack(20),
        ),
        Attack(
            title="Slicing Blade",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
