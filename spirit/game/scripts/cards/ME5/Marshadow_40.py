"""Marshadow (ME5 40 -- JP M5 038; English PBL/40). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.passives import effective_retreat_cost


def _defender_retreat(ctx) -> int:
    d = ctx.defender
    return effective_retreat_cost(ctx.board, d) if d is not None else 0


card = PokemonCardDef(
    guid="ec13f8ae-e84c-5eda-ae45-40f1e08e8ad1",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marshadow.Name",
    display_name="Marshadow",
    searchable_by=["Marshadow", "Basic"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=802,
    abilities=[
        Attack(
            title="Shadowy Knot",
            game_text="This attack does 30 damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="x",
            effect=ac.damage_per(_defender_retreat, 30),
        ),
    ],
)
