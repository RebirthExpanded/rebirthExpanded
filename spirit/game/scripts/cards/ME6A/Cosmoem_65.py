"""Cosmoem (ME6A 65 -- JP M6a 065; English 30C/79). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="ae611a90-014a-5eb6-9e40-82ab4d6d0178",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    display_name="Cosmoem",
    searchable_by=["Cosmoem", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=65,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmog.Name",
    family_id=789,
    abilities=[
        Attack(
            title="Stiffen",
            game_text="During your opponent's next turn, this Pokémon takes 60 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            effect=pc.protect_next_turn(reduce=60),
        ),
    ],
)
