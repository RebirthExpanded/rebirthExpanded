"""Noibat (SV09 127 -- JP SV9 080; English JTG/127, JTG/169). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="0e0aaae1-e078-532e-a7df-955f2a8f283e",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name",
    display_name="Noibat",
    searchable_by=["Noibat", "Basic"],
    subtypes=["Basic"],
    collector_number=127,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=714,
    abilities=[
        Attack(
            title="Rapid Draw",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=su.draw_attack(1),
        ),
    ],
)
