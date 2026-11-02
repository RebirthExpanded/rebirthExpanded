"""Leafeon (Promo_SWSH 191 -- JP SP 215; English SP/191). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.passives import effective_retreat_cost


def _defender_retreat(ctx) -> int:
    d = ctx.defender
    return effective_retreat_cost(ctx.board, d) if d is not None else 0


card = PokemonCardDef(
    guid="766d1415-68cd-56af-b6e7-49dcc9cc14dd",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Leafeon.Name",
    display_name="Leafeon",
    searchable_by=["Leafeon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=191,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Leaf Guard",
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=pc.protect_next_turn(reduce=30),
        ),
        Attack(
            title="Grass Knot",
            game_text="This attack does 30 more damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=ac.damage_per(_defender_retreat, 30, base=50),
        ),
    ],
)
