"""Squawkabilly (SV09 141 -- JP SVM 123; English JTG/141). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="6378156f-46d8-56fd-8653-4a5e1e4a7efa",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Squawkabilly.Name",
    display_name="Squawkabilly",
    searchable_by=["Squawkabilly", "Basic"],
    subtypes=["Basic"],
    collector_number=141,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=931,
    abilities=[
        Attack(
            title="Add On",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.draw_attack(2),
        ),
        Attack(
            title="Hyper Voice",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
