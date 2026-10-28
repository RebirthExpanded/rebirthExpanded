"""Rhyhorn (SV035 111 -- JP SV2a 111; English MEW/111). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="4aa4022c-c236-5c3e-a36b-39dae2ba5123",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyhorn.Name",
    display_name="Rhyhorn",
    searchable_by=["Rhyhorn", "Basic"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=111,
    abilities=[
        Attack(
            title="Push Down",
            game_text="Switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=su.gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Boulder Crush",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
