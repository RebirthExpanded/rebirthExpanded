"""Pikachu (ME6A 21 -- JP M6a 021; English 30C/27). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="fab8e35c-5ea9-525f-913c-435287622ad9",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Nap",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.heal_attack(30),
        ),
    ],
)
