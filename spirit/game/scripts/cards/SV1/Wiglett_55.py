"""Wiglett (SV1 55 -- JP SV1S 018; English PAF/121, SVI/206, SVI/55). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="83de33d2-e3ad-5b17-8170-846cbd9ed96d",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name",
    display_name="Wiglett",
    searchable_by=["Wiglett", "Basic"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=960,
    abilities=[
        Attack(
            title="Twisting Strike",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=pc.flip_protection(prevent=True, effects_too=True),
        ),
    ],
)
