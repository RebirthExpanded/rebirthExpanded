"""Braviary (SV08 153 -- JP SV7a 050; English SSP/153, SSP/214). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="9734c93f-770e-57b3-ae16-1db059e53211",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Braviary.Name",
    display_name="Braviary",
    searchable_by=["Braviary", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=153,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rufflet.Name",
    family_id=627,
    abilities=[
        Attack(
            title="Drag Off",
            game_text="Switch in 1 of your opponent's Benched Pokémon to the Active Spot. This attack does 40 damage to the new Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=su.gust_attack(damage_to_new_active=40),
        ),
        Attack(
            title="Blasting Wind",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
        ),
    ],
)
