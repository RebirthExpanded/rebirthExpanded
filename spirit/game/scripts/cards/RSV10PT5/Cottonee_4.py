"""Cottonee (RSV10PT5 4 -- JP SV11W 004; English WHT/4, WHT/90). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="2bbd331b-50c8-5465-befe-7f6ca8c48145",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    display_name="Cottonee",
    searchable_by=["Cottonee", "Basic"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=546,
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
