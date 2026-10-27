"""Seel (ME2 21 -- JP M2 021; English PFL/21). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="9327cc3e-74a6-5257-85f6-503802877564",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name",
    display_name="Seel",
    searchable_by=["Seel", "Basic"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=86,
    abilities=[
        Attack(
            title="Bubble Drain",
            game_text="Heal 20 damage from this Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=su.heal_attack(20),
        ),
    ],
)
