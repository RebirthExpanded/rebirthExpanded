"""Marnie's Scraggy (SV10 132 -- JP SVOM 003; English DRI/132). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="ecef95f1-5452-5a2e-becf-31c53bfecd7d",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesScraggy.Name",
    display_name="Marnie's Scraggy",
    searchable_by=["Marnie's Scraggy", "Basic"],
    subtypes=["Basic"],
    collector_number=132,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=559,
    abilities=[
        Attack(
            title="Crunch",
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=ac.discard_opponent_energy_attack(1),
        ),
    ],
)
