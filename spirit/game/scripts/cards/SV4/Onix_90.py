"""Onix (SV4 90 -- JP SV4M 039; English PAR/90). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="d200db59-c62d-5c87-ae2a-c85c4d1498cc",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    display_name="Onix",
    searchable_by=["Onix", "Basic"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=95,
    abilities=[
        Attack(
            title="Hard Headbutt",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=pc.flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Land Crush",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
