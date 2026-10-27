"""Marnie's Liepard (SV10 131 -- JP SVOM 002; English DRI/131). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _defender_ex(ctx) -> bool:
    return ctx.defender is not None and "ex" in (subtypes_for(ctx.defender.archetype_id) or [])


card = PokemonCardDef(
    guid="b0de8ae5-dd0c-5b75-b02c-9256228f5f87",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesLiepard.Name",
    display_name="Marnie's Liepard",
    searchable_by=["Marnie's Liepard", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=131,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesPurrloin.Name",
    family_id=509,
    abilities=[
        Attack(
            title="Pointy Claws",
            game_text="If your opponent's Active Pokémon is a Pokémon ex, this attack does 70 more damage.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=70,
            damage_operator="+",
            effect=ac.bonus_if(_defender_ex, 70),
        ),
    ],
)
