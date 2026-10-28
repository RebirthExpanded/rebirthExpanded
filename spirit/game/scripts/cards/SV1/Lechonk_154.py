"""Lechonk (SV1 154 -- JP SV1S 066; English SVI/154). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="dc2d9b70-ef89-582d-9162-c764f44e2487",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lechonk.Name",
    display_name="Lechonk",
    searchable_by=["Lechonk", "Basic"],
    subtypes=["Basic"],
    collector_number=154,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=915,
    abilities=[
        Attack(
            title="Repelling Odor",
            game_text="Switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Stampede",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
