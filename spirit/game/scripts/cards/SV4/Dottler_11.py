"""Dottler (SV4 11 -- JP SV4M 004; English PAR/11, PAR/184). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="3a213705-17a5-516d-9756-5e48610b1707",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dottler.Name",
    display_name="Dottler",
    searchable_by=["Dottler", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Blipbug.Name",
    family_id=824,
    abilities=[
        Attack(
            title="Protect",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=pc.flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Zen Headbutt",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
