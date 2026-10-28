"""Shroomish (SV1 3 -- JP SVAM 001; English SVI/3). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="de25f133-d65c-5b0f-baf7-70658d96043b",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name",
    display_name="Shroomish",
    searchable_by=["Shroomish", "Basic"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=285,
    abilities=[
        Attack(
            title="Absorb",
            game_text="Heal 10 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=su.heal_attack(10),
        ),
    ],
)
