"""Koraidon (SVP 14 -- JP WCS23 013; English SVI/124, SVP/14). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="0f6b42c7-fe22-5336-b2b7-268a45f7e194",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koraidon.Name",
    display_name="Koraidon",
    searchable_by=["Koraidon", "Basic"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=1007,
    abilities=[
        Attack(
            title="Claw Slash",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
        Attack(
            title="Rampaging Fang",
            game_text="Discard 3 Energy from this Pokémon.",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=ac.self_energy_discard_attack(count=3),
        ),
    ],
)
