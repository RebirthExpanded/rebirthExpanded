"""Horsea (SV065 10 -- JP SV6a 010; English SFA/10, SFA/67). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="982afe9f-8b76-55a3-889e-53266d3c6170",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name",
    display_name="Horsea",
    searchable_by=["Horsea", "Basic"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=116,
    abilities=[
        Attack(
            title="Hold Still",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.WATER: 1},
            effect=su.heal_attack(30),
        ),
        Attack(
            title="Razor Fin",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
