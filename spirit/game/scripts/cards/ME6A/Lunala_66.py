"""Lunala (ME6A 66 -- JP M6a 066; English 30C/80). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_energy_card


card = PokemonCardDef(
    guid="496e9edc-e9c2-5cec-bae8-5d620300e809",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lunala.Name",
    display_name="Lunala",
    searchable_by=["Lunala", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=66,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    family_id=789,
    abilities=[
        Attack(
            title="Midnight Ray",
            game_text="This attack does 20 more damage for each Energy card in your discard pile.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator="+",
            effect=ac.damage_per(ac.count_discard("mine", pred=is_energy_card), 20, base=20),
        ),
        Attack(
            title="Lunar Blast",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)
