"""Exeggcute (SV08 2 -- JP SV8 001; English SSP/2). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="5ce8f59a-6f87-544c-a84e-17499e68ebc3",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    display_name="Exeggcute",
    searchable_by=["Exeggcute", "Basic"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=102,
    abilities=[
        Attack(
            title="Absorb",
            game_text="Heal 10 damage from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=su.heal_attack(10),
        ),
    ],
)
