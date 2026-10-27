"""Heliolisk (SV08 155 -- JP SV8 089; English SSP/155). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import is_energy_card


card = PokemonCardDef(
    guid="f0ca0342-8d0b-549b-ad4b-5fd8cf70bdba",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heliolisk.Name",
    display_name="Heliolisk",
    searchable_by=["Heliolisk", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=155,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Helioptile.Name",
    family_id=694,
    abilities=[
        Attack(
            title="Parabolic Charge",
            game_text="Search your deck for up to 4 Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(is_energy_card, count=4, reveal=True, prompt="Choose up to 4 Energy cards."),
        ),
        Attack(
            title="Electroslug",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
