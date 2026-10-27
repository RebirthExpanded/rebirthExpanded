"""Squawkabilly (SV10 160 -- JP SV10 086; English DRI/160). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="530c5c39-e5c4-59e1-9370-ea9d096060e7",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Squawkabilly.Name",
    display_name="Squawkabilly",
    searchable_by=["Squawkabilly", "Basic"],
    subtypes=["Basic"],
    collector_number=160,
    set_code="SV10",
    regulation_mark="I",
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
            title="Push Down",
            game_text="You may switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=su.gust_attack(opponent_chooses=True),
        ),
    ],
)
