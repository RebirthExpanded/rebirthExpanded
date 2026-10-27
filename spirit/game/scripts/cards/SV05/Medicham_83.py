"""Medicham (SV05 83 -- JP SV5M 038; English TEF/83). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="61dd49e3-4deb-5152-9fc4-acda95eb12ff",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Medicham.Name",
    display_name="Medicham",
    searchable_by=["Medicham", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=83,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    family_id=307,
    abilities=[
        Attack(
            title="Low Sweep",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
        Attack(
            title="High Jump Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=110,
        ),
    ],
)
