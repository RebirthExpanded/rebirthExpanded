"""Mantine (SV08 40 -- JP SVLN 001; English SSP/40). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="709715c2-49e0-5cc6-b115-42e8c50b61fe",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mantine.Name",
    display_name="Mantine",
    searchable_by=["Mantine", "Basic"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=458,
    abilities=[
        Attack(
            title="Wave Splash",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
        Attack(
            title="Aqua Dive",
            game_text="This attack does 50 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            effect=ac.snipe_attack(50, pool="any"),
        ),
    ],
)
