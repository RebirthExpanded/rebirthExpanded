"""Metapod (SV035 11 -- JP SV2a 011; English MEW/11). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="da92c515-8769-5110-b900-327d3b6e9a1e",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name",
    display_name="Metapod",
    searchable_by=["Metapod", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name",
    family_id=10,
    abilities=[
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Defensive Posture",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage done to this Pokémon by attacks.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=pc.flip_protection(prevent=True),
        ),
    ],
)
