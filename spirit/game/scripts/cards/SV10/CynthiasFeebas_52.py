"""Cynthia's Feebas (SV10 52 -- JP SV9a 028; English DRI/52). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="febabdc0-352c-5205-b6ef-bfdd626e3dd9",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasFeebas.Name",
    display_name="Cynthia's Feebas",
    searchable_by=["Cynthia's Feebas", "Basic"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=349,
    abilities=[
        Attack(
            title="Undulate",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=pc.flip_protection(prevent=True, effects_too=True),
        ),
    ],
)
