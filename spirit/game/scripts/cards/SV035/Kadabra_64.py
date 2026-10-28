"""Kadabra (SV035 64 -- JP SV2a 064; English MEW/64, PAF/149). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="f8e5c19b-2f93-5c56-9bdb-40165c51f107",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kadabra.Name",
    display_name="Kadabra",
    searchable_by=["Kadabra", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Abra.Name",
    family_id=63,
    abilities=[
        Attack(
            title="Teleportation Attack",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=su.switch_self_attack(),
        ),
    ],
)
