"""Primeape (SV10 91 -- JP SV10 046; English DRI/91). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="40f702a5-05b8-564d-902b-6c280a0ab87b",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    display_name="Primeape",
    searchable_by=["Primeape", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=91,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    family_id=56,
    abilities=[
        Attack(
            title="Drag Off",
            game_text="Switch in 1 of your opponent's Benched Pokémon to the Active Spot. This attack does 30 damage to the new Active Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=su.gust_attack(damage_to_new_active=30),
        ),
    ],
)
