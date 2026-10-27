"""Milcery (ME2 43 -- JP MBD 007; English PFL/43). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="9869b394-c456-5725-8217-a984dbd68ace",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Milcery.Name",
    display_name="Milcery",
    searchable_by=["Milcery", "Basic"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=868,
    abilities=[
        Attack(
            title="Draining Kiss",
            game_text="Heal 10 damage from this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=su.heal_attack(10),
        ),
    ],
)
