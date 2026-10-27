"""Klang (ZSV10PT5 62 -- JP SV11W 066; English BLK/140, BLK/62). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="338b8db4-f2b0-5d26-b7e4-960512711945",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klang.Name",
    display_name="Klang",
    searchable_by=["Klang", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=62,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Klink.Name",
    family_id=599,
    abilities=[
        Attack(
            title="Hard Gears",
            game_text="During your opponent's next turn, this Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=pc.protect_next_turn(reduce=20),
        ),
    ],
)
