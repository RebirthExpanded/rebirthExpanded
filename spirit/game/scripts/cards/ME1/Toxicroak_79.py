"""Toxicroak (ME1 79 -- JP M1L 031; English MEG/79). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="113a3576-b95a-59f6-a3d0-c83e7d984669",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxicroak.Name",
    display_name="Toxicroak",
    searchable_by=["Toxicroak", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name",
    family_id=453,
    abilities=[
        Attack(
            title="Reckless Charge",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=70,
            effect=ac.recoil_attack(20),
        ),
    ],
)
