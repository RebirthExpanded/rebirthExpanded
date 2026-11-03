"""Suicune (XYPJ 510 -- JP CP5 010; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="6e5425b5-efe9-5680-be3d-013968cb609c",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name",
    display_name="Suicune",
    searchable_by=["Suicune", "Basic"],
    subtypes=["Basic"],
    collector_number=510,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=245,
    abilities=[
        Attack(
            title="Spiral Drain",
            game_text="Heal 20 damage from this Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=su.heal_attack(20),
        ),
        Attack(
            title="Aurora Beam",
            game_text="",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)
