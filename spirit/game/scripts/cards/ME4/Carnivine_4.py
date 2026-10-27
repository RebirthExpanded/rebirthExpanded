"""Carnivine (ME4 4 -- JP M4 004; English CRI/4). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.passives import effective_retreat_cost


def _no_retreat_cost(ctx) -> bool:
    d = ctx.defender
    return d is not None and effective_retreat_cost(ctx.board, d) == 0


card = PokemonCardDef(
    guid="3db9e848-a711-529e-939f-47654bc609c4",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carnivine.Name",
    display_name="Carnivine",
    searchable_by=["Carnivine", "Basic"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=455,
    abilities=[
        Attack(
            title="Chomp Whole",
            game_text="If your opponent's Active Pokémon has no Retreat Cost, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_no_retreat_cost, 80),
        ),
    ],
)
