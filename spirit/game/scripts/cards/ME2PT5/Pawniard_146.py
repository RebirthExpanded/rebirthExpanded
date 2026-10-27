"""Pawniard (ME2PT5 146 -- JP M2a 116; English ASC/146). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="2ca9b9a7-5b76-57e4-a42c-b2b754553246",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name",
    display_name="Pawniard",
    searchable_by=["Pawniard", "Basic"],
    subtypes=["Basic"],
    collector_number=146,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=624,
    abilities=[
        Attack(
            title="Push Down",
            game_text="Switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            effect=su.gust_attack(opponent_chooses=True),
        ),
    ],
)
