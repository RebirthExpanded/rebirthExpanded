"""Koraidon (SV07 90 -- JP SVI 033; English SCR/90). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _defender_ex(ctx) -> bool:
    return ctx.defender is not None and "ex" in (subtypes_for(ctx.defender.archetype_id) or [])


card = PokemonCardDef(
    guid="92d2760e-7d70-579c-9c11-55eb9292df31",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koraidon.Name",
    display_name="Koraidon",
    searchable_by=["Koraidon", "Basic"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=1007,
    abilities=[
        Attack(
            title="Resolute Fang",
            game_text="If your opponent's Active Pokémon is a Pokémon ex, this attack does 70 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
            damage_operator="+",
            effect=ac.bonus_if(_defender_ex, 70),
        ),
    ],
)
