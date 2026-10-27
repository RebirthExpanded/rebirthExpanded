"""Shelmet (SV09 12 -- JP SV9 008; English JTG/12). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="96b9dc93-9cfa-5c24-b8e5-0747300fcb64",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shelmet.Name",
    display_name="Shelmet",
    searchable_by=["Shelmet", "Basic"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=616,
    abilities=[
        Attack(
            title="Shell Smack",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage done to this Pokémon by attacks.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=pc.flip_protection(prevent=True),
        ),
    ],
)
