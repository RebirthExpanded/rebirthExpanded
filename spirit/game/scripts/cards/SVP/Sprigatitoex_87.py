"""Sprigatito ex (SVP 87 -- JP SVI 002; English ASC/251, SVP/87). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="84264159-a0d3-5807-8081-b2c5540dc403",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sprigatitoex.Name",
    display_name="Sprigatito ex",
    searchable_by=["Sprigatito ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=87,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=906,
    abilities=[
        Attack(
            title="Scratch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Magical Leaf",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=su.heal_attack(30),
        ),
    ],
)
