"""Shelgon (SV09 113 -- JP SV9 071; English JTG/113). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="a5126a7d-19b3-5db4-b390-120a402a4aba",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    display_name="Shelgon",
    searchable_by=["Shelgon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=113,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name",
    family_id=371,
    abilities=[
        Attack(
            title="Guard Press",
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=pc.protect_next_turn(reduce=30),
        ),
        Attack(
            title="Heavy Impact",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)
