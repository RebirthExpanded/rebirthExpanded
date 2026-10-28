"""Rookidee (SV2 164 -- JP SV2P 063; English PAL/164, PAL/225). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="a9714d73-53c9-5396-a873-bdbb68228688",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rookidee.Name",
    display_name="Rookidee",
    searchable_by=["Rookidee", "Basic"],
    subtypes=["Basic"],
    collector_number=164,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=821,
    abilities=[
        Attack(
            title="Send Back",
            game_text="Switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=su.gust_attack(opponent_chooses=True),
        ),
    ],
)
