"""Petilil (ZSV10PT5 6 -- JP SV11B 006; English BLK/6, BLK/91). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="8929d1f6-b8db-56bd-9e44-9599d608bf89",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name",
    display_name="Petilil",
    searchable_by=["Petilil", "Basic"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=548,
    abilities=[
        Attack(
            title="Hide",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pc.flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Leafage",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
