"""Absol (ME2 63 -- JP MBG 007; English PFL/63). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="63029126-98bc-506f-93e5-a9b95267fcbf",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Absol.Name",
    display_name="Absol",
    searchable_by=["Absol", "Basic"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=359,
    abilities=[
        Attack(
            title="Allure",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.draw_attack(2),
        ),
        Attack(
            title="Dark Cutter",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
