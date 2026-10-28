"""Charcadet (SV4 25 -- JP SV4K 013; English PAR/25). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="a97fda4f-a5f4-5d5f-a503-96e4328a2742",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    display_name="Charcadet",
    searchable_by=["Charcadet", "Basic"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=935,
    abilities=[
        Attack(
            title="Protect",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pc.flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Magma Punch",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
