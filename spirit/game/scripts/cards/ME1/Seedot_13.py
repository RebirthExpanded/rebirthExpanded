"""Seedot (ME1 13 -- JP M1L 007; English MEG/13). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="f8ca02de-2a49-5599-ba92-1f91117d22a7",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seedot.Name",
    display_name="Seedot",
    searchable_by=["Seedot", "Basic"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=273,
    abilities=[
        Attack(
            title="Nap",
            game_text="Heal 20 damage from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.heal_attack(20),
        ),
        Attack(
            title="Seed Bomb",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
