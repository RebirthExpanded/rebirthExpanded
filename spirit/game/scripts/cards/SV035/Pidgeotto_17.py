"""Pidgeotto (SV035 17 -- JP SV2a 017; English MEW/17, PAF/197). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="e666a0c3-c1eb-5877-90aa-080839059cc9",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name",
    display_name="Pidgeotto",
    searchable_by=["Pidgeotto", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgey.Name",
    family_id=16,
    abilities=[
        Attack(
            title="Flap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
