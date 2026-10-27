"""Klink (ZSV10PT5 61 -- JP SV11W 065; English BLK/139, BLK/61). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="5c27a630-b13b-5be1-8997-774e292d47a5",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klink.Name",
    display_name="Klink",
    searchable_by=["Klink", "Basic"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=599,
    abilities=[
        Attack(
            title="Hard Gears",
            game_text="During your opponent's next turn, this Pokémon takes 10 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            effect=pc.protect_next_turn(reduce=10),
        ),
    ],
)
