"""Toedscool (SV4 16 -- JP SV4M 007; English PAR/16). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="0bfed7cc-00d4-569a-a304-d210591eb86d",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name",
    display_name="Toedscool",
    searchable_by=["Toedscool", "Basic"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=948,
    abilities=[
        Attack(
            title="Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Absorb",
            game_text="Heal 20 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=su.heal_attack(20),
        ),
    ],
)
