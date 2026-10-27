"""Snom (ME1 42 -- JP M1S 024; English MEG/42). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="df813f0d-d3f7-5058-8c95-23c380000171",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snom.Name",
    display_name="Snom",
    searchable_by=["Snom", "Basic"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=872,
    abilities=[
        Attack(
            title="Hide",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.WATER: 1},
            effect=pc.flip_protection(prevent=True, effects_too=True),
        ),
    ],
)
