"""Marnie's Morpeko (SV10 137 -- JP SVOM 008; English DRI/137, SVP/206). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import PokemonTypes as _PT


card = PokemonCardDef(
    guid="c134b98f-d411-51ea-95b5-4bc5e541c6ba",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesMorpeko.Name",
    display_name="Marnie's Morpeko",
    searchable_by=["Marnie's Morpeko", "Basic"],
    subtypes=["Basic"],
    collector_number=137,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    family_id=877,
    abilities=[
        Attack(
            title="Spiky Wheel",
            game_text="This attack does 40 more damage for each Darkness Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("self", _PT.DARKNESS), 40, base=20),
        ),
    ],
)
