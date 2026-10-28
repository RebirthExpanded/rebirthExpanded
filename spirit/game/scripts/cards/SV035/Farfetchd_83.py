"""Farfetch'd (SV035 83 -- JP SV2a 083; English MEW/83). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="ddc2dff4-c32a-5125-8a3f-1bf44875056d",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Farfetchd.Name",
    display_name="Farfetch'd",
    searchable_by=["Farfetch'd", "Basic"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=83,
    abilities=[
        Attack(
            title="Package Deal",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.draw_attack(2),
        ),
        Attack(
            title="Leek Clobber",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
