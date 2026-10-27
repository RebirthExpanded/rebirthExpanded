"""Hop's Silicobra (SV09 86 -- JP SV9 053; English JTG/86). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import is_stadium_card


card = PokemonCardDef(
    guid="990dab07-70d4-5efb-95e3-234d0d8f0e07",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsSilicobra.Name",
    display_name="Hop's Silicobra",
    searchable_by=["Hop's Silicobra", "Basic"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=843,
    abilities=[
        Attack(
            title="Turf Maker",
            game_text="Search your deck for a Stadium card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(is_stadium_card, count=1, reveal=True, prompt="Choose a Stadium card."),
        ),
        Attack(
            title="Gnaw",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
