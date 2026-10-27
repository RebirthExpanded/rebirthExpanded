"""Applin (SV10 16 -- JP SV9a 009; English DRI/16). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="49b0cb4b-0786-5271-9f5f-4296675db9ce",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    display_name="Applin",
    searchable_by=["Applin", "Basic"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=840,
    abilities=[
        Attack(
            title="Mini Drain",
            game_text="Heal 10 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=su.heal_attack(10),
        ),
    ],
)
