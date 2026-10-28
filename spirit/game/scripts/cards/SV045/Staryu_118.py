"""Staryu (SV045 118 -- JP SV2a 120; English MEW/120, PAF/118). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="1658e42a-b327-5a18-b996-6fe04b71609f",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    display_name="Staryu",
    searchable_by=["Staryu", "Basic"],
    subtypes=["Basic"],
    collector_number=118,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=120,
    abilities=[
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness or Resistance, or by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.ignore_effects_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)
