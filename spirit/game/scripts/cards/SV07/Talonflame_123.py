"""Talonflame (SV07 123 -- JP SV7 085; English SCR/123). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.passives import effective_retreat_cost


def _heavy(ctx) -> bool:
    d = ctx.opponent_active()
    return d is not None and effective_retreat_cost(ctx.board, d) >= 2


card = PokemonCardDef(
    guid="122f7129-0909-5440-87d7-5a6b812a14c3",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Talonflame.Name",
    display_name="Talonflame",
    searchable_by=["Talonflame", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=123,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name",
    family_id=661,
    abilities=[
        Attack(
            title="Aero Chase",
            game_text="If the Retreat Cost of your opponent's Active Pokémon is ColorlessColorless or more, this attack does 110 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=110,
            damage_operator="+",
            effect=ac.bonus_if(_heavy, 110),
        ),
    ],
)
