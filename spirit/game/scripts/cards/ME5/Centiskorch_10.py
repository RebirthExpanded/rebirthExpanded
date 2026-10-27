"""Centiskorch (ME5 10 -- JP M5 009; English PBL/10). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="49af6147-b3a6-5352-acdc-9a7b01590e8d",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Centiskorch.Name",
    display_name="Centiskorch",
    searchable_by=["Centiskorch", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sizzlipede.Name",
    family_id=850,
    abilities=[
        Attack(
            title="Controlled Burn",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=ac.mill_attack(2),
        ),
        Attack(
            title="Heat Tackle",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=ac.recoil_attack(30),
        ),
    ],
)
