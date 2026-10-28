"""Shellder (SV035 90 -- JP SV2a 090; English MEW/90). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="7f73c540-b4c5-54ba-ba48-4053047d92fb",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shellder.Name",
    display_name="Shellder",
    searchable_by=["Shellder", "Basic"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=90,
    abilities=[
        Attack(
            title="Shell Press",
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            effect=pc.protect_next_turn(reduce=30),
        ),
    ],
)
