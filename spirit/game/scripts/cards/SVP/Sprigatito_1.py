"""Sprigatito (SVP 1 -- JP SVP 213; English SVP/1). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="751c0511-2fb8-5e09-9c1f-86b66e5e07a0",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sprigatito.Name",
    display_name="Sprigatito",
    searchable_by=["Sprigatito", "Basic"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=906,
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
