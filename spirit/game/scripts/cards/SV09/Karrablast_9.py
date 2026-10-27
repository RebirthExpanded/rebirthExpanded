"""Karrablast (SV09 9 -- JP SV9 007; English JTG/9). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="0084b5f9-bb00-5b76-a4cd-fb3e14d7d3ca",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name",
    display_name="Karrablast",
    searchable_by=["Karrablast", "Basic"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=588,
    abilities=[
        Attack(
            title="Push Down",
            game_text="Switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=su.gust_attack(opponent_chooses=True),
        ),
    ],
)
