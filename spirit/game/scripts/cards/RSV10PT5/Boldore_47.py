"""Boldore (RSV10PT5 47 -- JP SV11W 044; English WHT/128, WHT/47). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID


def _has_fighting_resistance(ctx) -> bool:
    defender = ctx.defender
    return defender is not None and \
        defender.get_attribute(AttrID.RESISTANCE_TYPES) == PokemonTypes.FIGHTING.value


card = PokemonCardDef(
    guid="54af212e-43d3-5e2c-82e2-27e1a2916d1e",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Boldore.Name",
    display_name="Boldore",
    searchable_by=["Boldore", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Roggenrola.Name",
    family_id=524,
    abilities=[
        Attack(
            title="Smack Down",
            game_text="If your opponent's Active Pokémon has Fighting Resistance, this attack does 50 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_has_fighting_resistance, 50),
        ),
        Attack(
            title="Power Gem",
            game_text="",
            cost={PokemonTypes.FIGHTING: 3},
            damage=90,
        ),
    ],
)
