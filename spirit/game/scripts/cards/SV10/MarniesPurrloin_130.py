"""Marnie's Purrloin (SV10 130 -- JP SVOM 001; English DRI/130). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _defender_ex(ctx) -> bool:
    return ctx.defender is not None and "ex" in (subtypes_for(ctx.defender.archetype_id) or [])


card = PokemonCardDef(
    guid="feb75f07-fc89-5ca4-b143-c5d902d19d1a",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesPurrloin.Name",
    display_name="Marnie's Purrloin",
    searchable_by=["Marnie's Purrloin", "Basic"],
    subtypes=["Basic"],
    collector_number=130,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=509,
    abilities=[
        Attack(
            title="Pointy Nails",
            game_text="If your opponent's Active Pokémon is a Pokémon ex, this attack does 40 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            damage_operator="+",
            effect=ac.bonus_if(_defender_ex, 40),
        ),
    ],
)
