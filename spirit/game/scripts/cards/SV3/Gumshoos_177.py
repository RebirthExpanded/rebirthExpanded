"""Gumshoos (SV3 177 -- JP SV1a 063; English OBF/177). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="8dd4223b-0d8d-56f9-ade7-4d2ff773ba9f",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gumshoos.Name",
    display_name="Gumshoos",
    searchable_by=["Gumshoos", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=177,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yungoos.Name",
    family_id=734,
    abilities=[
        Attack(
            title="Headbang",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Crunch",
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=ac.discard_opponent_energy_attack(1),
        ),
    ],
)
