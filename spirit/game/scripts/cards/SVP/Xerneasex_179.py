"""Xerneas ex (SVP 179 -- JP SVM 052; English SVP/179). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _defender_ex(ctx) -> bool:
    return ctx.defender is not None and "ex" in (subtypes_for(ctx.defender.archetype_id) or [])


card = PokemonCardDef(
    guid="a6b6dfe4-fdae-59d6-87d9-236b978cbc53",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xerneasex.Name",
    display_name="Xerneas ex",
    searchable_by=["Xerneas ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=179,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=716,
    abilities=[
        Attack(
            title="Aurora Beam",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Rising Horns",
            game_text="If your opponent's Active Pokémon is a Pokémon ex, this attack does 100 more damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=ac.bonus_if(_defender_ex, 100),
        ),
    ],
)
